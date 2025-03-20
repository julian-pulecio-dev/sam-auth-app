from dataclasses import dataclass, fields

class EventRequest:
    def __new__(cls, *args, **kwargs):
        # Validar los argumentos antes de crear la instancia
        cls_fields = {field.name for field in fields(cls)}
        unexpected_fields = {k: v for k, v in kwargs.items() if k not in cls_fields}
        
        if unexpected_fields:
            raise TypeError(f"unexpected fields: {unexpected_fields}")

        return super().__new__(cls)
    