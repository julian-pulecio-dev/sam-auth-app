from dataclasses import dataclass, InitVar
from models.event_headers import EventHeaders
from models.event_body import EventBody

@dataclass
class EventRequest:
    event: InitVar[dict]
    
    def __post_init__(self, event:dict):
        self.event_headers, self.event_body = self.validate(event)

    def _get_headers(self, event:dict) -> EventHeaders:
        """Validate headers."""
        try:
            print('ev:', event)
            headers = EventHeaders(
                headers=event.get("headers"),
            )
            return headers
        except TypeError as e:
            raise ValueError(f"Header validation error: {e}")

    def _get_body(self, event:dict) -> EventBody:
        """Validate body."""
        try:
            body = EventBody(
                body=event.get("body"),
                is_base64_encoded=event.get("isBase64Encoded")
            )
            return body
        except TypeError as e:
            raise ValueError(f"Body validation error: {e}")

    def validate(self, event:dict) -> tuple[EventHeaders, EventBody]:
        """Validate both headers and body."""
        event_headers = self._get_headers(event)
        event_body = self._get_body(event)
        return event_headers, event_body

    


