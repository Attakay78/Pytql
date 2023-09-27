import json
from .exceptions import UnsupportedDataType


class DataConverter(object):
    def __new__(cls, data, file, column_length):
        """creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, data, file, column_length):
        """Class for parsing and preparing data for proper table display.

        Args:
            data (_type_): Data to be prepared for display.
            file (_type_): File containing the data to be prepared for display.
            column_length (_type_): Table column length.
        """

        self.data = data
        self.file = file
        self.column_length = column_length

    def parse(self):
        """Parses data from different data type to list

        Raises:
            UnsupportedDataType: Raises if data type is not supported.
            ValueError: Raises if data or file not provided or file is empty.

        Returns:
            List: List of data to be populated in the table.
        """
        if self.data != None:
            if isinstance(self.data, dict):
                data = self._fill_missing_values(list(self.data.values()))
                data = self._transpose_data(data)
                return data
            elif isinstance(self.data, list):
                data = self._fill_missing_values(self.data)
                return data
            else:
                raise UnsupportedDataType(
                    message="Data type is not supported, provide list | dict."
                )
        elif self.file != None:
            with open(self.file) as fp:
                file_data = json.load(fp)

                if len(file_data) > 0:
                    if isinstance(file_data[0], list):
                        data = self._fill_missing_values(file_data)
                        return data
                    elif isinstance(file_data[0], dict):
                        dict_data = []
                        for row_data in file_data:
                            dict_data.append(list(row_data.values()))
                        return dict_data
                else:
                    raise ValueError(f"File `{self.file}` is empty.")
        else:
            raise ValueError("Data or file needs to be provided to file table.")

    def validate_data(self, data, fields):
        """Function to valiate whether data values matches with their field properties.

        Args:
            data (_type_): Data to be validated.
            fields (_type_): Fields used to validate the data.
        """
        field_types = list(fields.values())

        for row_index, row_data in enumerate(data):
            for column_index, column_data in enumerate(row_data):
                field_types[column_index].validate_field_props(
                    column_data, row_index, column_index
                )

    def match_added_row_to_table(self, row):
        """Function to match newly added row to the table. Pads all missing table fields with 
        None value.

        Args:
            row (_type_): Row to be added to the table.
        Returns:
            List: List of augmented row data.
        """
        row = row + ([None] * (self.column_length - len(row)))
        return row

    def _fill_missing_values(self, data):
        """Function for padding all missing table fields with None value.

        Args:
            data (_type_): Data to be checked.

        Returns:
           List[List]: List of augmented list rows.
        """
        for index, row in enumerate(data):
            data[index] = row + ([None] * (self.column_length - len(row)))

        return data

    def _transpose_data(self, data):
        """Function to transpose data. Function used to swap columns and rows.
        Ideally for converting m*n matrix to n*m matrix

        Args:
            data (_type_): Data to be transposed.

        Returns:
            List[List]: List of augmented list data.
        """
        new_data = []
        for column_index in range(len(data[0])):
            new_row = []

            for row in data:
                new_row.append(row[column_index])

            new_data.append(new_row)
        return new_data
