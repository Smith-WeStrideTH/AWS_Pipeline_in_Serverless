import json
import boto3
import base64
from decimal import Decimal

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1') # update region if needed
    table_name = 'TemperatureSensor'
    table = dynamodb.Table(table_name)

    process_records= 0
    failed_records = 0
    items = []

    for record in event['Records']:
        try:
            data = record['kinesis']['data']
            data = base64.b64decode(data).decode('ascii') # return string
            data = json.loads(data,parse_float=Decimal)
            items.append({'PutRequest':{'Item':data}})
            process_records +=1
        except Exception as e:
            print(f'Error processing record: {e}')
            failed_records +=1

    batch_size = 1
    bathches = []
    for i in range(0, len(items),batch_size):
        bathches.append(items[i:i+batch_size])

    for batch in bathches:
        params = {'RequestItems': {table_name:batch}}
        response = dynamodb.batch_write_item(**params)
    return{
        'processed_records':process_records,
        'failed_records':failed_records
    }


