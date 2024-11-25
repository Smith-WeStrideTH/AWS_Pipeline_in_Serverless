import boto3
client = boto3.client('ec2')

resp = client.terminate_instances(InstanceIds=['i-04c8b118f30095c13'])

for instance in resp['TerminatingInstances']:
    print(f"The instance with id {instance['InstanceId']} is terminated")