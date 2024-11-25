import boto3

client = boto3.client("s3")
file = open('2_Hands_on_Boto3_and_S3/1_create_s3.py').read()
response = client.put_object(
    ACL='private',
    Body=file,
    Bucket='mycreatedbucketfromvscode1234a',
    Key='folder/1_create_s3.py'
)
