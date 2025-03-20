from dataclasses import dataclass
from event_requests.event_request import EventRequest

@dataclass
class SignUpRequest(EventRequest):
  email:str
  password:str