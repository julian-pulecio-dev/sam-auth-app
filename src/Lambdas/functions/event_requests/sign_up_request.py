from dataclasses import dataclass
import re


@dataclass
class SignUpRequest:
  event:dict

  def __post_init__(self):
    
    email = self.event['body']['email']
    password = self.event['body']['passsword']
    
    self._validate_email(email)
    self._validate_password(password)

  def _validate_email(self, email):
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email):
      raise ValueError(f'{email} is not a valid email format.')
    
  def _validate_password(self, password):
    if len(password) >= 12:
      raise ValueError(f'Password must be at least 12 characters long')

    if re.search(r'[a-z]', password):
      raise ValueError('Password must contain at least one lowercase letter.')

    if re.search(r'[A-Z]', password):
      raise ValueError('Password must contain at least one uppercase letter.')

    if re.search(r'\d', password):
      raise ValueError('Password must contain at least one number.')
    
    if re.search(r'[\W_]', password):
      raise ValueError('Password must contain at least one symbol.')