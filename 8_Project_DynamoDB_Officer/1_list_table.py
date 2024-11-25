import boto3

dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

# table.table_name.all()
table_names = [table.table_name for table in dynamodb.tables.all()]

if table_names:
    print("Show list of all table:")
    for table_name in table_names:
        print(table_name)

else:
    print("There is no table on this region")
print('-----'*10)