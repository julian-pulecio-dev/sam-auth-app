from dataclasses import dataclass, InitVar
from models.event_headers import EventHeaders
from models.event_body import EventBody
from exceptions.request_exception import RequestException
from event_requests.event_request import EventRequest


@dataclass
class EventValidator:
    event: InitVar[dict]
    
    def __post_init__(self, event:dict):
        try:
            self.event_headers, self.event_body = self.validate(event)
        except TypeError as e:
            raise RequestException(str(e), status_code=400)

    def _validate_headers(self, event:dict) -> EventHeaders:
        headers = EventHeaders(
            headers=event.get("headers"),
        )
        return headers
        
    def _validate_body(self, event:dict) -> EventBody:
        body = EventBody(
            body=event.get("body"),
            is_base64_encoded=event.get("isBase64Encoded")
        )
        return body
    
    def validate_request(self, request:EventRequest):
        try:
            request = request(**self.event_body.data)
            return request
        except TypeError as e:
            print('my exception: ', e.args, e.__context__, )
            raise RequestException(
                message=str(e),
                status_code=400
            )
        
    def validate(self, event:dict) -> tuple[EventHeaders, EventBody]:
        event_headers = self._validate_headers(event)
        event_body = self._validate_body(event)
        return event_headers, event_body

    


