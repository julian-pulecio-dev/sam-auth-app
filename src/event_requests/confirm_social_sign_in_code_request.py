from dataclasses import dataclass
from event_requests.event_request import EventRequest
from exceptions.request_exception import RequestException
import re


@dataclass
class ConfirmSocialSignInCodeRequest(EventRequest):
  code:str
  provider:str

  def _validate(self):
    pass
  
  