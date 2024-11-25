import boto3
client = boto3.client('ec2')

FILTER_INSTANCE = [{
    'Name': 'tag:Department',
    'Values': ['DataAnalyst']
}]

resp = client.describe_instances(Filters=FILTER_INSTANCE)

for reservation in resp["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["InstanceId"])
