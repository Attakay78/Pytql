class ColumnDoesNotExist(Exception):
    """Exception class to raise if column does not exist"""

    pass


class FieldTypeError(Exception):
    """Exception class to raise if field type is not supported"""

    pass


class MaxLengthExceeded(Exception):
    """Exception class to raise if max length is exceeded"""

    pass


class FieldCantBeNull(Exception):
    """Exception class to raise if field expected not to be null is null"""

    pass


class UnsupportedDataType(Exception):
    """Exception class to raise if data type is not supported"""

    pass


class HeadersRequired(Exception):
    """Exception class to raise if headers  are required but missing"""

    pass
