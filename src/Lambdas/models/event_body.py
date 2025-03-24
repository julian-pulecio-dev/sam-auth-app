from dataclasses import dataclass, field, InitVar
from models.event_headers import EventHeaders
from urllib.parse import parse_qs
from exceptions.unsupported_media_type import UnsupportedMediaTypeException
import base64
import json


@dataclass
class EventBody:
    headers: InitVar[EventHeaders]
    body: InitVar[str] = field(metadata={"alias": "Body"})
    is_base64_encoded: InitVar[bool] = field(metadata={"alias": "isBase64Encoded"})

    def __post_init__(self, headers:EventHeaders, body:str, is_base64_encoded:bool):
        if is_base64_encoded:
            parsed_body = base64.b64decode(body).decode('utf-8')
        else: 
            parsed_body = self._parse_body(headers.content_type, body)
            
        self.data = parsed_body

    def _parse_body(self, content_type:str, body:str):
        if content_type == 'application/json':
            parsed_body = json.loads(body)
        elif content_type == 'application/x-www-form-urlencoded':
            parsed_body = { key: value[0] if value else None for key,value in parse_qs(body).items()}
        elif content_type == 'text/plain':
            parsed_body = body
        else:
            raise UnsupportedMediaTypeException('Unsupported Media Type')
        return parsed_body
        