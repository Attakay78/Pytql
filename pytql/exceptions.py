class UnsupportedDataType(Exception):
    def __init__(self, message="Unsupported data type, provide [list, dict]"):
        super().__init__(message)


class HeadersRequired(Exception):
    def __init__(self, message="Headers required"):
        super().__init__(message)
