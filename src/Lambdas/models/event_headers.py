from dataclasses import dataclass, field, InitVar
from exceptions.request_exception import RequestException

@dataclass
class EventHeaders:
  headers: InitVar[dict] = field(metadata={"alias": "Headers"})

  def __post_init__(self, headers:dict):
    if 'Content-Type' not in headers:
      raise RequestException(f"Header validation error Content-Type not found")
    self.content_type = headers.get('Content-Type')
    