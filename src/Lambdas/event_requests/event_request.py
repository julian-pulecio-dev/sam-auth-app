from dataclasses import dataclass, fields
from exceptions.request_exception import RequestException
from abc import ABC, abstractmethod
import re


@dataclass
class EventRequest(ABC):
    def __new__(cls, *args, **kwargs):
        cls_fields = {field.name for field in fields(cls)}
        required_fields = {field.name for field in fields(cls) if field.default == field.default_factory == field.default}
        kwargs = set(kwargs.keys())

        cls._validate_missing_fields(required_fields, kwargs)
        cls._validate_unexpected_fields(cls_fields, kwargs)

        return super().__new__(cls)
    
    @abstractmethod
    def _validate(self):
        pass
    
    @classmethod
    def _validate_unexpected_fields(cls, cls_fields:set, kwargs:set)->None:
        unexpected_fields = kwargs.difference(cls_fields)
        if unexpected_fields:
            raise RequestException(f'unexpected fields were found on the request :{list(unexpected_fields)}') 
    
    @classmethod
    def _validate_missing_fields(cls, required_fields:set, kwargs:set)->None:
        missing_fields = required_fields.difference(kwargs)
        if missing_fields:
            raise RequestException(f'Missing fields were found on the request: {list(missing_fields)}')