import boto3

client = boto3.client("s3")

response = client.list_buckets()
list_bucket = []
for bucket in response['Buckets']:
    list_bucket.append(bucket['Name'])


paginator = client.get_paginator('list_objects_v2')
# empty all bucket
for bucket in list_bucket:
    for page in paginator.paginate(Bucket=bucket):
        for content in page.get('Contents', []):
            client.delete_object(Bucket=bucket, Key=content['Key'])

# delete all bucket
for bucket in list_bucket:
    response = client.delete_bucket(
        Bucket=bucket,
    )
