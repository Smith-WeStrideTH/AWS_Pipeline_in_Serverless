import boto3

dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

table = dynamodb.Table('employees')
table.put_item(Item=
               {
                   'id' : '1',
                   'timestamp': '2022-10-12',
                   'name': 'Smith',
                   'gender': 'Male',
                   'age' : 40,
                   'position' : 'Data Science'
               })