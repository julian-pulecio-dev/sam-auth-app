from event_requests.sign_in_custom_auth_request import SignInCustomAuthRequest
from decorators.event_validator import event_validator
from models.user_pool import UserPool
from headers import get_headers
import json


@event_validator(SignInCustomAuthRequest)
def lambda_handler(event:SignInCustomAuthRequest, context):    
    user_pool = UserPool(
        client='cognito-idp'
    )
    response = user_pool.sign_in_custom_auth(
        email=event.email
    )
    return {
        "statusCode": 200,
        "headers": get_headers(),
        "body": json.dumps(response)
    }
