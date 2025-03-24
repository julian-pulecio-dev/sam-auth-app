from event_requests.event_validator import EventValidator
from exceptions.request_exception import RequestException
from botocore.exceptions import ClientError
import logging
import json

logger = logging.getLogger()


def event_validator(request_class:type):
    def decorator(function):
        def wrapper(event, context):
            print('ev:', event)
            try:
                event_validator = EventValidator(event)
                event_request = event_validator.validate_request(request=request_class)
                result = function(event_request, context)
                return result
            except ClientError as e:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": str(e)})
                }
            except RequestException as e:
                return {
                    "statusCode": e.status_code,
                    "body": json.dumps({"error": str(e)})
                }
            
        return wrapper
    return decorator