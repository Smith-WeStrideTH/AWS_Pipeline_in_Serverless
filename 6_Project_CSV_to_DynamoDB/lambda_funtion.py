import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')


# bucket_name = event['Records'][0]['s3']['bucket']['name']
# key_name = event['Records'][0]['s3']['object']['key']
bucket_name = 'csvdatahandle-id123a'
key_name = 'employees.csv'
file_object =  s3_client.get_object(Bucket=bucket_name,Key=key_name)
data = file_object['Body'].read().decode('utf-8')
data = data.split('\n')
dict = [emp.split(',') for emp in data]

for i in range(len(dict)):
    try:
        table.put_item(Item = {
            "id": dict[i][0],
            'name': dict[i][1],
            'gender':dict[i][2]
        })
    except Exception as e:
        print(e)
