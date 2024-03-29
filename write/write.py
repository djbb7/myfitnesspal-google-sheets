import gspread
import os
from datetime import date, timedelta
import json
from oauth2client.service_account import ServiceAccountCredentials

def lambda_handler(event, context):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('serviceaccount.json', scope)

    gc = gspread.authorize(credentials)

    sheet = gc.open_by_url(os.environ['sheet_url']).worksheet("PROGRESS TRACKER")

    values = sheet.col_values(11)

    row = len(values) + 1
    
    if row % 9 == 8:
        row += 2
    elif row % 9 == 0:
        row += 1

    cells = sheet.range('A'+str(row)+':K'+str(row))
    cells[0].value = str(date.today() - timedelta(1))
    cells[2].value = cells[2].value.replace('\'','')
    #cells[3].value = bodyfat
    cells[4].value = event['calories']
    cells[5].value = event['protein']
    cells[6].value = event['carbohydrates']
    cells[7].value = event['fat']
    cells[10].value = '.'

    sheet.update_cells(cells)

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
