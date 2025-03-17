from dataclasses import dataclass, field, InitVar
import base64
import json

# Define the expected structure of the body
@dataclass
class EventBody:
    body: InitVar[str] = field(metadata={"alias": "Body"})
    is_base64_encoded: InitVar[bool] = field(metadata={"alias": "isBase64Encoded"})

    def __post_init__(self, body:str, is_base64_encoded:bool):
        if is_base64_encoded:
            body = base64.b64decode(body).decode('utf-8')
        self.data = json.loads(body)
        