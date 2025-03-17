import boto3
import os
import json
from event_requests.sign_up_request import SignUpRequest
from decorators.lambda_handler import decorator_factory

client = boto3.client('cognito-idp')
USER_POOL_CLIENT = os.environ.get('USER_POOL_CLIENT')

@decorator_factory(SignUpRequest)
def lambda_handler(event, context):
    print(event)
    return {
      "statusCode": 200,
      "body": 'success'
    }
