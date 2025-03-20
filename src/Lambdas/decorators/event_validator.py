from event_requests.event_validator import EventValidator
from exceptions.request_exception import RequestException


def event_validator(request_class:type):
    def decorator(function):
        def wrapper(event, context):
            try:
                event_validator = EventValidator(event)
                event_request = event_validator.validate_request(request=request_class)
                result = function(event_request, context)
                return result
            except RequestException as e:
                return {
                    "statusCode": e.status_code,
                    "body": str(e)
                }
                
        return wrapper
    return decorator