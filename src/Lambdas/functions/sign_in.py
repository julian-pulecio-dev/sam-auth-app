from event_requests.sign_in_request import SignInRequest
from decorators.event_validator import event_validator
from models.user_pool import UserPool
import json


@event_validator(SignInRequest)
def lambda_handler(event:SignInRequest, context):
    user_pool = UserPool(
        client='cognito-idp'
    )
    response = user_pool.sign_in(
        email=event.email,
        password=event.password
    )
    return {
      "statusCode": 200,
      "body": json.dumps(response)
    }
