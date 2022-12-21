class BaseException(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class UnsupportedDataType(BaseException):
    pass


class HeadersRequired(BaseException):
    pass


class ColumnDoesNotExist(BaseException):
    pass
