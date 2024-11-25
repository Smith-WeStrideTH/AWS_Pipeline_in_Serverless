import boto3

s3_client = boto3.client('s3')

def lambda_handler(event,context):
    try:
        bucket_name = event["Records"][0]['s3']['bucket']['name']
        object_name = event["Records"][0]['s3']['object']['key']
        # Delete object
        s3_client.delete_object(Bucket=bucket_name,Key=object_name)
        print("Successfully Delete File")
        return True
    except Exception as e:
        print(e)
        return False
