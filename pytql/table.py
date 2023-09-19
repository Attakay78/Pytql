# External imports
from copy import deepcopy

# Internal imports
from .data import Data
from .colors import Color
from .data_converter import DataConverter
from .model import Model
from .exceptions import ColumnDoesNotExist


class Table(object):
    """
    A class used to create Table data type.
    """

    def __init__(
        self,
        model: Model,
        data=None,
        file=None,
        header_color=Color.default,
        row_color=Color.default,
        table_color=Color.default,
    ):
        """
        Parameters
        ----------
        headers: List, Optional
            A collection of table headers.
        data: Union[List,Tuple, Set, Dictionary], Optional
            The data to be populated in the table.
        header_color: Color
            Color for the header
        row_color: Color
            Color for the rows
        table_color: Color
            Color for the table design
        """
        model = model()
        self.__model_fields = model._model_fields
        self.__headers = model._headers

        self.__data_converter = DataConverter(
            data=data, file=file, column_length=len(self.__headers)
        )
        parsed_data = self.__data_converter.parse()
        self.__data_converter.validate_data(data=parsed_data, fields=self.__model_fields)
        self.__data = Data(data=parsed_data, headers=self.__headers)

        self.__max_field_widths = []
        self.__gap_length = 3
        self.__gap = " " * self.__gap_length
        self.__filter_column = None
        self.__header_color = header_color
        self.__row_color = row_color
        self.__table_color = table_color

    def __max_width(self):
        # Calculates the maximum width of the table.

        total_width = 0
        for width in self.__max_field_widths:
            total_width += width
        return total_width + (len(self.__max_field_widths) - 1) * self.__gap_length

    def __get_max_field_width(self, column_index, data):
        # Calculates the maximum width of each field of the table.

        row_length = len(data)

        def _get_max_width(loop_length, mod_type="even"):
            # Calculates the maximum width for each field column in the table
            # Using left and right pointers to reduce the number of iterations in the row
            max_width = 0
            for index in range(loop_length):
                if (mod_type == "odd") and (index == loop_length - 1):
                    last_val_size = len(str(data[index][column_index]))
                    max_width = (
                        max_width if max_width > last_val_size else last_val_size
                    )
                else:
                    left_val_size = len(str(data[index][column_index]))
                    right_val_size = len(
                        str(data[row_length - index - 1][column_index])
                    )
                    max_val = (
                        left_val_size
                        if left_val_size > right_val_size
                        else right_val_size
                    )
                    max_width = max_width if max_width > max_val else max_val

            return max_width

        if row_length % 2 == 0:
            return _get_max_width(row_length // 2)
        else:
            return _get_max_width((row_length // 2) + 1, mod_type="odd")

    def __draw_header(self):
        # Drawing table header using string formatting
        format_header = ""
        for index, header in enumerate(self.__headers):
            if index == 0:
                format_header += f"{self.__header_color}{header:{self.__max_field_widths[index]}s}{Color.color_terminate}"
            else:
                format_header += f"{self.__header_color}{self.__gap}{header:{self.__max_field_widths[index]}s}{Color.color_terminate}"
        return format_header

    def __draw_row(self, data):
        # Drawing table rows using string formatting
        for row in data:
            format_row = ""
            for index, cell in enumerate(row):
                if index == 0:
                    format_row += f"{self.__row_color}{str(cell):{self.__max_field_widths[index]}s}{Color.color_terminate}"
                else:
                    format_row += f"{self.__row_color}{self.__gap}{str(cell):{self.__max_field_widths[index]}s}{Color.color_terminate}"

            print(format_row)

    def draw_table(self, data):
        """
        Draws table with data provided.

        Args:
            data (List): Table Data to be drawn

        Returns:
            None.
        """
        data.insert(0, self.__headers)
        self.__max_field_widths = []
        for column_index in range(len(data[0])):
            self.__max_field_widths.append(self.__get_max_field_width(column_index, data))

        data.pop(0)

        heading = self.__draw_header()
        print(f"{self.__table_color}{'=' * self.__max_width()}{Color.color_terminate}")
        print(heading)
        print(f"{self.__table_color}{'=' * self.__max_width()}{Color.color_terminate}")

        self.__draw_row(data=data)
        print("\n")

    def add_row(self, row, position=None):
        """
        Add row data to table.

        Args:
            row (List): Row to be added to table.
            position (Integer): Position of the new row.

        Returns:
            None.
        """
        new_row = self.__data_converter.match_added_row_to_table(row=row)
        self.__data_converter.validate_data(data=[new_row], fields=self.__model_fields)

        def _position_row(new_row=new_row):
            if position:
                self.__data.data.insert(position, new_row)
            else:
                self.__data.data.insert(len(self.__data.data), new_row)

        new_row_length = len(row)
        table_column_length = len(self.__data.data[0])

        if new_row_length == table_column_length:
            _position_row()
        elif new_row_length > table_column_length:
            # If new row data column fields is greater than current table fields,
            # slice away the extra field data
            _position_row(row[:table_column_length])
        else:
            # If new row data fields is less then current table fields, add None
            # to missing field data
            missing_cells = [
                "None" for _ in range(table_column_length - new_row_length)
            ]
            _position_row(row + missing_cells)

    def add_headers(self, headers):
        """
        Add header names to table.

        Args:
            headers (List): Headers to be added to table.

        Returns:
            None
        """
        pass

    def __column_exist(self, column):
        # Checks if column to be altered exists
        # and returns True otherwise False
        if column in self.__headers:
            self.__filter_column = column
            self.__data.filter_column = column
            return True

        raise ColumnDoesNotExist(f"Column name `{column}` does not exist.")

    def update(self, column):
        """
        Specifies the table column to update.

        Args:
            Column (String): Column to be updated.

        Returns:
            Table | None
        """
        column_exist = self.__column_exist(column)
        if column_exist:
            return self

        return None

    def where(self, value, updated_value):
        """
        Specifies which table data to alter.

        Args:
            value (String): Current value in table.
            updated_value (String): New value to replace old table value.
        """
        filter_column_index = self.__headers.index(self.__filter_column)

        for row in self.__data.data:
            if str(row[filter_column_index]) == str(value):
                row[filter_column_index] = updated_value

    def query(self):
        """
        Opens up the table for querying/filtering.

        Returns:
            Data
        """
        return deepcopy(self.__data)

    def get_data(self):
        """
        Returns current state of table data

        Returns:
            List
        """
        return self.__data.data
