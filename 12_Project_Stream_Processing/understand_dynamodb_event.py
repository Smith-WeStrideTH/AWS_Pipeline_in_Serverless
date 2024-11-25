import boto3

dynamodb = boto3.client('dynamodb',region_name='us-east-1')

data = {'Temperature': {'N': '45.02'},
         'expires': {'N': '1718245807.55555'}, 
         'user_id': {'S': 'e3e70682-c209-4cac-a29f-6fbed82c07cd'}, 
         'user_name': {'S': 'IoT-Device'}, 
         'company': {'S': 'ห้างหุ้นส่วนจำกัด ธาราธร'}, 
         'job': {'S': 'Temperature'}, 
         'timestamp': {'N': '1718245207.55555'}}

dynamodb.put_item(TableName='archivedata',Item=data)



'''
client  syntax
{'UserName' : {'S' : UserName}}

resource syntax
{'UserName' : Username}

'''

