from dataclasses import dataclass, field
from event_requests.event_request import EventRequest


@dataclass
class SignInRequest(EventRequest):
  email:str
  password:str

  def _validate(self):
    pass
