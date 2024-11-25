import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
table = dynamodb.Table('employees')


filter_key = {
    'id' : '1',
    'timestamp' :'2023-10-12'
}

data =table.get_item(Key=filter_key)
print(data['Item'])
print("-------"*10)

query_key_condtion = Key('id').eq('1') & Key('timestamp').gt('2022')
query_data = table.query(KeyConditionExpression=query_key_condtion)
print(query_data['Items'])
print("-------"*10)


