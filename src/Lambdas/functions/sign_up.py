import boto3
import os
import json
from event_requests.sign_up_request import SignUpRequest
from Lambdas.decorators.event_validator import event_validator

client = boto3.client('cognito-idp')
USER_POOL_CLIENT = os.environ.get('USER_POOL_CLIENT')

@event_validator(SignUpRequest)
def lambda_handler(event, context):
    print(event)
    return {
      "statusCode": 200,
      "body": 'success'
    }
