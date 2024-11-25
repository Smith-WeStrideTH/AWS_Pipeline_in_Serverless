import boto3
def lambda_handler(event,cotnext):
    client = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    # bucket = 'imagehandle-id123',
    # key = 'lambda1.png'
    file_type = key.split('.') 
    if len(file_type) > 1 :
        file_type = file_type[-1]
    else:
        file_type = -1 
    return str(file_type)
    # return{
    #     "fileType": str(file_type)
    # }
