from event_requests.confirm_social_sign_in_code_request import ConfirmSocialSignInCodeRequest
from decorators.event_validator import event_validator
from urllib3 import PoolManager
from urllib.parse import urlencode
from models.secret_manager import SecretManager
from headers import get_headers
import json


@event_validator(ConfirmSocialSignInCodeRequest)
def lambda_handler(event: ConfirmSocialSignInCodeRequest, context):    
    print('event:', event.code)

    secret_manager = SecretManager()
    secret = secret_manager.get_secret(secret_name='google_api_credentials')

    http = PoolManager()

    token_url = 'https://oauth2.googleapis.com/token'
    payload = {
        'code': event.code,
        'client_id': secret['client_id'],
        'client_secret': secret['client_secret'],
        'redirect_uri': 'postmessage',
        'grant_type': 'authorization_code'
    }

    body = urlencode(payload).encode('utf-8')

    response = http.request(
        'POST',
        token_url,
        body=body,
        headers={
          'Content-Type': 'application/x-www-form-urlencoded',
        }
    )

    response = json.loads(response.data.decode('utf-8'))

    return {
        "statusCode": 200,
        "headers": get_headers(),
        "body": json.dumps({
            "accessToken": response.get("access_token"),
            "idToken": response.get("id_token"),
            "refreshToken": response.get("refresh_token")
        })
    }