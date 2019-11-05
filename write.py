import gspread
import os
import datetime
from oauth2client.service_account import ServiceAccountCredentials

def lambda_handler(event, context):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('serviceaccount.json', scope)

    gc = gspread.authorize(credentials)

    sheet = gc.open_by_url(os.environ['sheet_url']).worksheet("PROGRESS TRACKER")

    values = sheet.col_values(3)

    row = len(values) + 1
    
    if row % 9 == 8:
        row += 2
    else if row % 9 == 0:
        row += 1

    cells = sheet.range('A'+str(row)+':H'+str(row))
    cells[0].value = str(datetime.date.today())
    #cells[2].value = weight
    #cells[3].value = bodyfat
    cells[4].value = event['calories']
    cells[5].value = event['protein']
    cells[6].value = event['carbohydrates']
    cells[7].value = event['fat']

    sheet.update_cells(cells)
