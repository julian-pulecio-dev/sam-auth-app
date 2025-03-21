from dataclasses import dataclass, field
from event_requests.event_request import EventRequest

@dataclass
class SignUpRequest(EventRequest):
  password:str
  email:str