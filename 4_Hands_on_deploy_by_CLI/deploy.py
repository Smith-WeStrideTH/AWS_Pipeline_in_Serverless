import json
import boto3

client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name =event["Records"][0]["s3"]["bucket"]["name"]
    file_name = event["Records"][0]["s3"]["object"]["key"]
    json_object = client.get_object(Bucket=bucket_name,Key=file_name)
    json_reader = json_object['Body'].read()
    json_dict = json.loads(json_reader)
    print(json_dict)
    # Process .....
    bucket_destination = 'targetjson1234a'
    response = client.copy_object(
        Bucket=bucket_destination,
        CopySource={'Bucket': bucket_name, 'Key': file_name},
        Key=file_name
    )

#aws lambda update-function-code --function-name s3event --s3-bucket handsons3event1234a --s3-key 4_Hands_on_deploy_by_CLI.zip --publish
# aws lambda update-function-code --function-name s3event --s3-bucket handsons3event1234a --s3-key 4_Hands_on_deploy_by_CLI.zip --publish



  

