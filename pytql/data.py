from .exceptions import ColumnDoesNotExist


class Data(object):
    def __init__(self, data=None, headers=None):
        """Class used to handle table data.

        Args:
            data (_type_, optional): Table data. Defaults to None.
            headers (_type_, optional): Table headers. Defaults to None.
        """
        self.data = data
        self._headers = headers
        self._filter_column = None

    def _operation(self, op_type, value):
        """Function for filtering operation types and performing those operations.

        Args:
            op_type (_type_): Operation type to be performed.
            value (_type_): Value to be filtered against.

        Returns:
            Data : An instance of Data.
        """
        filter_column_index = self._headers.index(self._filter_column)
        temp_data = self.data.copy()

        for row in temp_data:
            if op_type == "greater_than":
                if (row[filter_column_index] == None) or (
                    int(row[filter_column_index]) < int(value)
                ):
                    self.data.remove(row)
            elif op_type == "less_than":
                if (row[filter_column_index]) or (
                    int(row[filter_column_index]) > int(value)
                ):
                    self.data.remove(row)
            elif op_type == "equals":
                if row[filter_column_index] != value:
                    self.data.remove(row)
            else:
                print("Invalid operation type")
                return None

        return self

    def _column_exist(self, column):
        """Function to check if column to be filtered exist.

        Args:
            column (_type_): Column to be filtered.

        Returns:
            Boolean : True if column exist else Raises an ColumnDoesNotExist Exception.
        """
        if column in self._headers:
            self._filter_column = column
            return True

        raise ColumnDoesNotExist(f"Column name `{column}` does not exist.")

    def filter_by(self, column):
        """
        Filters table according to column name passed.

        Args:
            column (String): Column to be filtered.

        Returns:
            Data | None
        """
        column_exist = self._column_exist(column)
        if column_exist:
            return self

        return None

    def greater_than(self, value):
        """
        Filters the table data by value greater than provided.

        Args:
            value (String): value to be filter by.

        Returns:
            Data | None
        """
        return self._operation("greater_than", value)

    def less_than(self, value):
        """
        Filters the table data by value less than provided.

        Args:
            value (String): value to be filter by.

        Returns:
            Data | None
        """
        return self._operation("less_than", value)

    def equals(self, value):
        """
        Filters the table data by value equal to value provided.

        Args:
            value (String): value to be filter by.

        Returns:
            Data | None
        """
        return self._operation("equals", value)

    def end_query(self):
        """
        Ends table quering session.

        Returns:
            List
        """
        return self.data
