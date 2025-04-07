from event_requests.sign_up_request import SignUpRequest
from decorators.event_validator import event_validator
import json
import os
import requests


def lambda_handler(event, context):    
    print('event:',event)
    return {
      "statusCode": 200,
      "headers": {
        "Access-Control-Allow-Origin": os.environ.get("ALLOWED_ORIGIN", "http://localhost:3000"),
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Accept,Accept-Encoding,Accept-Language,User-Agent,Access-Control-Allow-Origin",
        "Content-Type": "application/json"
      },
      "body": json.dumps(event)
    }
