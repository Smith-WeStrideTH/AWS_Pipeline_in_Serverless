import boto3
ec2 = boto3.resource('ec2')

def lambda_handler(event,context):
    Filters=[
        {
            'Name': 'tag:Type', 
            'Values': ['Schedule']
            }
        ]
    instances = ec2.instances.filter(Filters=Filters)
    for instance in instances:
        instance.start()
    return "Successfully Runing Instances"

        
