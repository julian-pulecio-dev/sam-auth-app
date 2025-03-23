from dataclasses import dataclass, InitVar
from exceptions.request_exception import RequestException
from botocore.exceptions import ClientError
import boto3
import os

USER_POOL_CLIENT = os.environ.get('USER_POOL_CLIENT')

@dataclass
class UserPool:
  client:InitVar[str]

  def __post_init__(self, client:str):
    self.client = boto3.client(client)

  def sign_up(self, email:str, password:str):
    try:
      response = self.client.sign_up(
        ClientId=USER_POOL_CLIENT,
        Username=email,
        Password=password, 
      )
      return response
    except self.client.exceptions.UsernameExistsException as e:
      raise RequestException('Username with thr requested email already exists.')
  
  def confirm_sign_up(self, email:str, confirmation_code:str):
    try:
      response = self.client.confirm_sign_up(
        ClientId=USER_POOL_CLIENT,
        Username=email,
        ConfirmationCode=confirmation_code
      )
      return response
    except Exception as e:
      raise e
  
  
        