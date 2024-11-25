import boto3

client = boto3.client("s3")

response = client.select_object_content(
    Bucket='mycreatedbucketfromvscode1234a',
    Key='data_for_sql.csv',
    Expression='SELECT s.name  FROM s3object s',
    ExpressionType='SQL',
    InputSerialization={
        'CSV': {
            'FileHeaderInfo': 'USE',
        }
    },
    OutputSerialization={
        'JSON': {
        },
    }
)

for event in response['Payload']:
    if 'Records' in event:
        print(event["Records"]["Payload"].decode())
