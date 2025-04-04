from dataclasses import dataclass, InitVar
from models.event_headers import EventHeaders
from models.event_body import EventBody
from exceptions.request_exception import RequestException
from event_requests.event_request import EventRequest
from utils.utils import get_case_insensitive_value
from json import JSONDecodeError


@dataclass
class EventValidator:
    event: InitVar[dict]
    
    def __post_init__(self, event:dict):
        self.event_headers, self.event_body = self.validate(event)

    def _validate_headers(self, event:dict) -> EventHeaders:
        headers = EventHeaders(
            headers=get_case_insensitive_value(event,"headers"),
        )
        print('headers:', headers.content_type)
        return headers
        
    def _validate_body(self, event:dict, headers:EventHeaders) -> EventBody:
        body = EventBody(
            headers=headers,
            body=get_case_insensitive_value(event,"body"),
            is_base64_encoded=get_case_insensitive_value(event,"isBase64Encoded")
        )
        print('body:', body.data)
        return body
    
    def validate_request(self, request:EventRequest):
        if self.event_body.data: 
            request = request(**self.event_body.data)
        else:
            request = request(self.event_body.data)
        return request
        
    def validate(self, event:dict) -> tuple[EventHeaders, EventBody]:
        try:
            event_headers = self._validate_headers(event)
            event_body = self._validate_body(event, event_headers)
            return event_headers, event_body
        except JSONDecodeError as e:
            raise RequestException(e)


    


