from event_requests.confirm_sign_up_request import ConfirmSignUpRequest
from decorators.event_validator import event_validator
from models.user_pool import UserPool
import json
import os

@event_validator(ConfirmSignUpRequest)
def lambda_handler(event:ConfirmSignUpRequest, context):
    user_pool = UserPool(
        client='cognito-idp'
    )
    response = user_pool.confirm_sign_up(
        email=event.email,
        confirmation_code=event.confirmation_code
    )
    return {
      "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": os.environ.get("ALLOWED_ORIGIN", "http://localhost:3000"),
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Accept,Accept-Encoding,Accept-Language,User-Agent,Access-Control-Allow-Origin",
            "Content-Type": "application/json"
        },
      "body": json.dumps(response)
    }
