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
            data = json.loads(json.dumps(data),parse_float=Decimal)
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

event = {
  "Records": [
    {
      "kinesis": {
        "partitionKey": "partitionKey-03",
        "data": {'user_id': 'e3e70682-c209-4cac-a29f-6fbed82c07cd', 
                 'timestamp': 1718184320.643952, 
                 'company': 'ห้างหุ้นส่วนจำกัด ธาราธร', 
                 'job': 'Temperature', 
                 'user_name': 'IoT-Device', 
                 'Temperature': 39.82, 
                 'expires': 17181849920.643952
         },

      }
    }
  ]
}






print(lambda_handler(event,context=None))
    

