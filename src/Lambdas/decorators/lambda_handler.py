from event_requests.event_request import EventRequest

def decorator_factory(request_type:type):
    def decorator(function):
        def wrapper(event, context):
            event_request = EventRequest(event)
            request = request_type(**event_request.event_body.data)
            result = function(request, context)
            return result
        return wrapper
    return decorator