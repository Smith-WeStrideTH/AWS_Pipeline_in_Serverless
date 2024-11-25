import boto3

def lambda_handler(event,context):
    s3_client = boto3.client('s3')
    try: 
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        soruce_object_key = event['Records'][0]['s3']['object']['key']
        destination_bucket = 'imagedatas3-destination-id1234a'
        # Copy Object
        copy_source = {'Bucket': source_bucket, 'Key':soruce_object_key}
        s3_client.copy_object(CopySource=copy_source, Key=soruce_object_key, Bucket=destination_bucket)
        return {
            'bucket': source_bucket,
            'key': soruce_object_key
        }
    except Exception as e:
        print(e)
        return None