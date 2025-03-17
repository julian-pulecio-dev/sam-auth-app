from dataclasses import dataclass, field, InitVar
from typing import Optional

@dataclass
class EventHeaders:
  headers: InitVar[dict] = field(metadata={"alias": "Headers"})

  def __post_init__(self, headers:dict):
    if 'Content-Type' not in headers:
      raise ValueError(f"Header validation error:")
    self.content_type = headers.get('Content-Type')
    