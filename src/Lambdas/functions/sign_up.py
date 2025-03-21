import boto3
import os
from event_requests.sign_up_request import SignUpRequest
from decorators.event_validator import event_validator

client = boto3.client('cognito-idp')
USER_POOL_CLIENT = os.environ.get('USER_POOL_CLIENT')

@event_validator(SignUpRequest)
def lambda_handler(event:SignUpRequest, context):
    print(event)
    return {
      "statusCode": 200,
      "body": 'success'
    }
