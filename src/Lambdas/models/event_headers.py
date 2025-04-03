from dataclasses import dataclass, field, InitVar
from exceptions.request_exception import RequestException
from utils.utils import get_case_insensitive_value

@dataclass
class EventHeaders:
  headers: InitVar[dict] = field(metadata={"alias": "headers"})

  def __post_init__(self, headers:dict):
    content_type = get_case_insensitive_value(headers,'content-type')
    print('content-type:', content_type)
    if content_type is None:
      raise RequestException(f"Header validation error content-type not found")
    self.content_type = content_type
    