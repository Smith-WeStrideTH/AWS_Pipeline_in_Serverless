import boto3

client = boto3.client("s3")
response = client.list_objects(
    Bucket='mycreatedbucketfromvscode1234a'
)

for key in response['Contents']:
    print(key["Key"])