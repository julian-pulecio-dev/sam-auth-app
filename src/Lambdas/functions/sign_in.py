from event_requests.sign_in_request import SignInRequest
from decorators.event_validator import event_validator
from models.user_pool import UserPool
import os
import json


@event_validator(SignInRequest)
def lambda_handler(event:SignInRequest, context):
    user_pool = UserPool(
        client='cognito-idp'
    )
    print(event.email)
    print(event.password)
    response = user_pool.sign_in(
        email=event.email,
        password=event.password
    )
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": os.environ.get("ALLOWED_ORIGIN", "http://localhost:5173"),
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Accept,Accept-Encoding,Accept-Language,User-Agent,Access-Control-Allow-Origin",
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }
