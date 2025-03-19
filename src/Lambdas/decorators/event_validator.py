from Lambdas.event_requests.event_validator import EventValidator

def event_validator(request_type:type):
    def decorator(function):
        def wrapper(event, context):
            event_request = EventValidator(event)
            request = request_type(**event_request.event_body.data)
            result = function(request, context)
            return result
        return wrapper
    return decorator