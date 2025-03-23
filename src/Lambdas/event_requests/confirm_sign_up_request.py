from dataclasses import dataclass
from event_requests.event_request import EventRequest
from exceptions.request_exception import RequestException
import re


@dataclass
class ConfirmSignUpRequest(EventRequest):
  email:str
  confirmation_code:str

  def __post_init__(self):
    self._validate()

  def _validate(self):
    self._validate_email(self.email)
  
  def _validate_email(self, email:str):
    if not re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
      raise RequestException(f'{email} email do not match the email format example@email.com')