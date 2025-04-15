from event_requests.event_validator import EventValidator
from exceptions.request_exception import RequestException
from botocore.exceptions import ClientError
import logging
import json
import os

logger = logging.getLogger()


def event_validator(request_class:type):
    def decorator(function):
        def wrapper(event, context):
            print('ev:', event)
            try:
                event_validator = EventValidator(event)
                event_request = event_validator.validate_request(request=request_class)
                print('event_request:', event_request)
                result = function(event_request, context)
                return result
            except ClientError as e:
                print('e:', e)
                return {
                    "statusCode": 400,
                    "headers": {
                        "Access-Control-Allow-Origin": os.environ.get("ALLOWED_ORIGIN", "http://localhost:5173"),
                        "Access-Control-Allow-Credentials": "true",
                        "Access-Control-Allow-Methods": "POST, OPTIONS",
                        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Accept,Accept-Encoding,Accept-Language,User-Agent",
                        "Content-Type": "application/json"
                    },
                    "body": json.dumps({"error": str(e)})
                }
            except RequestException as e:
                print('e:', e)
                return {
                    "statusCode": e.status_code,
                    "headers": {
                        "Access-Control-Allow-Origin": os.environ.get("ALLOWED_ORIGIN", "http://localhost:5173"),
                        "Access-Control-Allow-Credentials": "true",
                        "Access-Control-Allow-Methods": "POST, OPTIONS",
                        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,Accept,Accept-Encoding,Accept-Language,User-Agent",
                        "Content-Type": "application/json"
                    },
                    "body": json.dumps({"error": str(e)})
                }
            
        return wrapper
    return decorator