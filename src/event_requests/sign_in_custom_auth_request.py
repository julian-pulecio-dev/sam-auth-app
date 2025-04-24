from dataclasses import dataclass, field
from event_requests.event_request import EventRequest


@dataclass
class SignInCustomAuthRequest(EventRequest):
  email:str

  def _validate(self):
    pass
