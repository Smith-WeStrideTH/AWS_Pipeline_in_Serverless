import boto3
import json

def lambda_handler(event,context):
    step_functions_client = boto3.client('stepfunctions')
    state_machine_arn = 'arn:aws:states:us-east-1:471112977094:stateMachine:MyStateMachine-ovwn7mn60'
    step_functions_client = boto3.client('stepfunctions')
    params = {
        'stateMachineArn': state_machine_arn,
        'input' :json.dumps(event)
    }
    response = step_functions_client.start_execution(**params)
