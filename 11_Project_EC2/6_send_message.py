import boto3
sns = boto3.client('sns')

def lambda_handler(event,context):
    TopicArn = 'arn:aws:sns:us-east-1:471112977094:EC2-Alert_Stopped'
    sns.publish(
        TopicArn=TopicArn,
        Subject='EC2 has Stopped',
        Message= 'server has stopped please take a look!'
    )