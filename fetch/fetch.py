import myfitnesspal
import boto3
import json
import os
from datetime import date, timedelta

def lambda_handler(event, context):
    yesterday = date.today() - timedelta(1)
    client = myfitnesspal.Client(os.environ['user'], os.environ['password'])
    data = client.get_date(yesterday.year, yesterday.month, yesterday.day)

    client = boto3.client('lambda')

    client.invoke(
            FunctionName='savetosheets',
            InvocationType='Event',
            Payload=json.dumps(data.totals))

    return {
        'statusCode': 200,
        'body': json.dumps(data.totals)
    }
