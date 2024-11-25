import boto3

def lambda_handler(event,context):
    dynamodb = boto3.client('dynamodb',region_name='us-east-1') # updated if needed
    target_table = 'archivedata'
    process_count = 0

    for record in event['Records']:
        if record['eventName'] == 'REMOVE':
            old_image = record['dynamodb']['OldImage']
            print(old_image)
            try :
                dynamodb.put_item(TableName=target_table, Item=old_image)
                process_count +=1
            except Exception as e:
                print(f"Error processing record: {e}")
    return f"Successfully processed {process_count} records"
