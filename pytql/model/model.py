from ..fields import Field

# Model base class
class Model:
    def __init__(self):
        # get dict value of subclasses and set model field values
        subclass_dict = self.__class__.__dict__.copy()
        self._model_fields = {}

        # check the base classes of all the props in subclass_dict and add to the model_fields
        # all props with base Field
        for prop, value in subclass_dict.items():
            base_classes = value.__class__.__bases__
            if base_classes and (Field in base_classes):
                self._model_fields[prop] = value

        self._headers = []
        # Set table header names
        for field_name in self._model_fields:
            if self._model_fields[field_name].field_name:
                self._headers.append(self._model_fields[field_name].field_name)
            else:
                self._headers.append(field_name)
