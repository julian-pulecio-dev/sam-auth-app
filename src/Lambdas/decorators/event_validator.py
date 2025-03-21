from event_requests.event_validator import EventValidator
from exceptions.request_exception import RequestException
import logging
import json

logger = logging.getLogger()


def event_validator(request_class:type):
    def decorator(function):
        def wrapper(event, context):
            try:
                event_validator = EventValidator(event)
                event_request = event_validator.validate_request(request=request_class)
                result = function(event_request, context)
                return result
            except RequestException as e:
                logger.error(f"Validation failed: {e}")
                return {
                    "statusCode": e.status_code,
                    "body": json.dumps({"error": str(e)})
                }
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                return {
                    "statusCode": 500,
                    "body": json.dumps({"error": "Internal Server Error"})
                }
                
        return wrapper
    return decorator