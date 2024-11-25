import boto3

dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
table = dynamodb.Table('employees')

user_lists = [
    {
    'id' : '1',
    'timestamp': '2023-10-12',
    'name': 'Smith',
    'gender': 'Male',
    'age' : 40,
    'position' : 'Data Science'
    },
        {
    'id' : '2',
    'timestamp': '2022-5-12',
    'name': 'John',
    'gender': 'Male',
    'age' : 24,
    'position' : 'Data Science'
    },
        {
    'id' : '3',
    'timestamp': '2022-1-12',
    'name': 'Korn',
    'gender': 'Female',
    'age' : 42,
    'position' : 'Data Analyst'
    },
]
with table.batch_writer() as batch:
    for user in user_lists:
        batch.put_item(Item=user)


