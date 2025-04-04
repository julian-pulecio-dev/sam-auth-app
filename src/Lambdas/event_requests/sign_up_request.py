from dataclasses import dataclass, field
from event_requests.event_request import EventRequest
from exceptions.request_exception import RequestException
import re

@dataclass
class SignUpRequest(EventRequest):
  email:str
  password:str

  def __post_init__(self):
    self._validate()

  def _validate(self):
    self._validate_email(self.email)
    self._validate_password(self.password)

  def _validate_email(self, email:str):
    if not re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
      raise RequestException(f'{email} emails do not match the email format example@email.com')

  def _validate_password(self, password:str):
    errors = []
    if len(password) < 12:
      errors.append(f'Password must be at least 12 characters long')
 
    if not re.search(r'[a-z]', password):
      errors.append('Password must contain at least one lowercase letter.')
 
    if not re.search(r'[A-Z]', password):
      errors.append('Password must contain at least one uppercase letter.')
 
    if not re.search(r'\d', password):
      errors.append('Password must contain at least one number.')
     
    if not re.search(r'[\W_]', password):
      errors.append('Password must contain at least one symbol.')
    
    if errors:
      raise RequestException(errors)