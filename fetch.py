import myfitnesspal
from datetime import date, timedelta

def lambda_handler(event, context):
    yesterday = date.today() - timedelta(1)
    client = myfitnesspal.Client(os.environ['user'], os.environ['password'])
    data = client.get_date(yesterday.year, yesterday.month, yesterday.day)
