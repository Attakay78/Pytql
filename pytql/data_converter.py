from .exceptions import UnsupportedDataType


class DataConverter(object):
    def __new__(cls, data, headers):
        """creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, data, headers):
        """
        Parameters
        ----------
        headers: List, Optional
            A collection of table headers.
        data: Union[List,Tuple, Set, Dictionary], Optional
            The data to be populated in the table.
        """

        self.data = data
        self.headers = headers
        self.default_headers = None

    def parse(self):
        """
        Parses data from different data type to list

        Returns:
            Tuple | List
        """
        if isinstance(self.data, dict):
            data = self._fill_missing_values(list(self.data.values()))
            data = self._transpose_data(data)
            if self.headers:
                return data
            else:
                return (list(self.data.keys()), data)
        elif isinstance(self.data, list):
            data = self._fill_missing_values(self.data)
            if self.headers:
                return (self.headers, data)
            else:
                default_headers = [
                    "Column" + str(field_data) for field_data in range(len(data[0]))
                ]
                self.default_headers = default_headers
                return (default_headers, data)
        else:
            raise UnsupportedDataType(
                message="Data type is not supported, provide list | dict."
            )

    def _fill_missing_values(self, data):
        # Function to padding all missing table fields with None value.
        max_length = max([len(row) for row in data])

        for index, row in enumerate(data):
            data[index] = row + (["None"] * (max_length - len(row)))

        return data

    def _transpose_data(self, data):
        # Function used to swap columns and rows.
        # Ideally for converting m*n matrix to n*m matrix
        new_data = []
        for column_index in range(len(data[0])):
            new_row = []

            for row in data:
                new_row.append(row[column_index])

            new_data.append(new_row)
        return new_data
