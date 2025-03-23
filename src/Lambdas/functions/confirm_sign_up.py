from event_requests.confirm_sign_up_request import ConfirmSignUpRequest
from decorators.event_validator import event_validator
from models.user_pool import UserPool
import json


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
      "body": json.dumps(response)
    }
