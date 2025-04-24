from dataclasses import dataclass, InitVar
from exceptions.request_exception import RequestException
from botocore.exceptions import ClientError
import boto3
import os
import json

USER_POOL_CLIENT = os.environ.get('USER_POOL_CLIENT')

@dataclass
class SecretManager:
  def __post_init__(self):
    session = boto3.session.Session()
    self.client =  session.client(
        service_name='secretsmanager',
        region_name='us-east-1'
    )


  def get_secret(self, secret_name:str):
    get_secret_value_response = self.client.get_secret_value(
        SecretId=secret_name
    )
    print(json.loads(get_secret_value_response['SecretString']) )
    return json.loads(get_secret_value_response['SecretString'])       