from ..exceptions import FieldTypeError, MaxLengthExceeded, FieldCantBeNull
from typing import Any, Optional


# Field descriptor for setting fields for columns
class Field:
    def __init__(
        self,
        name: Optional[str] = None,
        nullable: bool = True,
        # default: Optional[Any] = None,
        unique: bool = False,  # TODO
        editable: bool = True,  # TODO
        serialize: bool = True,  # TODO
    ):
        self.field_name = name
        self.is_nullable = nullable
        # self.default = default
        self.is_unique = unique
        self.is_editable = editable
        self.is_serializable = serialize

    def _check_is_nullable(self, value: Any, row_index, column_index):
        if self.is_nullable == False and value == None:
            msg: str = f"Table[Row:{row_index}, Column:{column_index}]: Field `{self.name}` can't be null."
            raise FieldCantBeNull(msg)

    def _check_type_validity(self, value: str, row_index, column_index, field_type):
        if type(value) != field_type and value != None:
            msg: str = (
                f"Table[Row:{row_index}, Column:{column_index}]: Expected type of value {value} is"
                f"`{field_type}` but `{type(value)}` given."
            )
            raise FieldTypeError(msg)

    def __set_name__(self, owner, name: str):
        if self.field_name:
            self.name = self.field_name
        else:
            self.name = name

    def validate_field_props(self, value, row_index, column_index, field_type):
        self._check_type_validity(value, row_index, column_index, field_type)
        self._check_is_nullable(value, row_index, column_index)


class CharField(Field):
    def __init__(
        self,
        max_length: int = 225,
        name: Optional[str] = None,
        nullable: bool = True,
        # default: Optional[Any] = None,
        unique: bool = False,  # TODO
        editable: bool = True,  # TODO
        serialize: bool = True,  # TODO
        choices: Optional[Any] = None,  # TODO
    ):

        super().__init__(
            name=name,
            nullable=nullable,
            unique=unique,
            editable=editable,
            serialize=serialize,
        )
        self.max_length = max_length
        self.max_allowable_size = 225
        self.choices = choices

    def _check_max_length(self, value: Any, row_index, column_index):
        if value != None:
            # We are assuming value has been checked for nullability. If the value passed the check to
            # this stage then no need to check it's max length
            if self.max_length and self.max_length > self.max_allowable_size:
                msg: str = f"Maximum allowable size for CharField is {self.max_allowable_size}, but got {self.max_length}."
                raise MaxLengthExceeded(msg)

            if self.max_length and len(value) > self.max_length:
                msg: str = (
                    f"Table[Row:{row_index}, Column:{column_index}]: Maximum length exceeded, value "
                    f"`{value}` expected max of {self.max_length}, but got {len(value)}."
                )
                raise MaxLengthExceeded(msg)

    def validate_field_props(self, value, row_index, column_index):
        super().validate_field_props(value, row_index, column_index, str)
        self._check_max_length(value, row_index, column_index)


class TextField(CharField):
    def __init__(
        self,
        max_length: int = 1024,
        name: Optional[str] = None,
        nullable: bool = True,
        # default: Optional[Any] = None,
        unique: bool = False,  # TODO
        editable: bool = True,  # TODO
        serialize: bool = True,  # TODO
        choices: Optional[Any] = None,  # TODO
    ):

        super().__init__(
            name=name,
            nullable=nullable,
            unique=unique,
            editable=editable,
            serialize=serialize,
            choices=choices,
        )
        self.max_length = max_length
        self.max_allowable_size = 1024
        self.choices = choices


class IntField(Field):
    def validate_field_props(self, value, row_index, column_index):
        super().validate_field_props(value, row_index, column_index, int)


class BooleanField(Field):
    def validate_field_props(self, value, row_index, column_index):
        super().validate_field_props(value, row_index, column_index, bool)


class FloatField(Field):
    def validate_field_props(self, value, row_index, column_index):
        super().validate_field_props(value, row_index, column_index, float)
