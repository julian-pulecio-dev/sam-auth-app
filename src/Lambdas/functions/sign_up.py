from event_requests.sign_up_request import SignUpRequest
from decorators.event_validator import event_validator
from models.user_pool import UserPool
import boto3
import os
import json


@event_validator(SignUpRequest)
def lambda_handler(event:SignUpRequest, context):    
    user_pool = UserPool(
        client='cognito-idp'
    )
    response = user_pool.sign_up(
        email=event.email,
        password=event.password
    )
    return {
      "statusCode": 200,
      "body": json.dumps(response)
    }
