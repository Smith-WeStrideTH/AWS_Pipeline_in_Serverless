import boto3

client = boto3.client("s3")

response = client.create_bucket(
    ACL='private',
    Bucket='mycreatedbucketfromvscode1234a',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1'
    }
)
