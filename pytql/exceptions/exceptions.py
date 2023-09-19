class ColumnDoesNotExist(Exception):
    pass


class FieldTypeError(Exception):
    pass


class MaxLengthExceeded(Exception):
    pass


class FieldCantBeNull(Exception):
    pass


class UnsupportedDataType(Exception):
    pass


class HeadersRequired(Exception):
    pass
