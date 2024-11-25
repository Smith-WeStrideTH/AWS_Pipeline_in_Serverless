import boto3
ec2 = boto3.resource('ec2')
# for instance in ec2.instances.all():
#     print(f"Instance ID {instance.instance_id}, Instance Type {instance.instance_type}")

# FILTER_INSTANCE = [{
#     'Name' : 'availability-zone',
#     'Values': ['us-east-1b']
# }]
# for instance in ec2.instances.filter(Filters=FILTER_INSTANCE):
#     print(f"Instance ID {instance.instance_id}, Instance Type {instance.instance_type}")

FILTER_INSTANCE = [{
    'Name': 'instance-state-name',
    'Values' : ['running']
}]
ec2.instances.filter(Filters=FILTER_INSTANCE).stop()


