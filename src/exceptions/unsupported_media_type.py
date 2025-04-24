from exceptions.request_exception import RequestException

class UnsupportedMediaTypeException(RequestException):
    def __init__(self, message):
        super().__init__(message)
        self.status_code = 415 