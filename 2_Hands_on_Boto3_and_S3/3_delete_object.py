import boto3

client = boto3.client("s3")
response = client.delete_object(
    Bucket='mycreatedbucketfromvscode1234a',
    Key='folder/1_create_s3.py'
)