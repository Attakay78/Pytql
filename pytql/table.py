# External imports
from copy import deepcopy

# Internal imports
from .data import Data
from .colors import Color


class Table(object):
    """
    A class used to create Table data type.
    """

    def __init__(
        self,
        headers=None,
        data=None,
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

        self.headers = headers
        self.max_field_widths = []
        self.gap_length = 3
        self.gap = " " * self.gap_length
        self.data_instance = Data(data=data, headers=headers)
        self.filter_column = None
        self.header_color = header_color
        self.row_color = row_color
        self.table_color = table_color

    def _max_width(self):
        # Calculates the maximum width of the table.

        total_width = 0
        for width in self.max_field_widths:
            total_width += width
        return total_width + (len(self.max_field_widths) - 1) * self.gap_length

    def _get_max_field_width(self, column_index, data):
        # Calculates the maximum width of each field of the table.

        row_length = len(data)

        def _get_max_width(loop_length, mod_type="even"):
            # Calculates the maximum width for each field column in the table
            # Using 2 pointer tp reduce the number of iterations in the row
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

    def _draw_header(self):
        # Drawing table header using string formatting
        format_header = ""
        for index, header in enumerate(self.headers):
            if index == 0:
                format_header += f"{self.header_color}{header:{self.max_field_widths[index]}s}{Color.color_terminate}"
            else:
                format_header += f"{self.header_color}{self.gap}{header:{self.max_field_widths[index]}s}{Color.color_terminate}"
        return format_header

    def _draw_row(self, data):
        # Drawing table rows using string formatting
        for row in data:
            format_row = ""
            for index, cell in enumerate(row):
                if index == 0:
                    format_row += f"{self.row_color}{str(cell):{self.max_field_widths[index]}s}{Color.color_terminate}"
                else:
                    format_row += f"{self.row_color}{self.gap}{str(cell):{self.max_field_widths[index]}s}{Color.color_terminate}"

            print(format_row)

    def draw_table(self, data):
        """
        Draws table with data provided.

        Args:
            data (List): Table Data to be drawn

        Returns:
            None.
        """
        data.insert(0, self.headers)
        self.max_field_widths = []
        for column_index in range(len(data[0])):
            self.max_field_widths.append(self._get_max_field_width(column_index, data))

        data.pop(0)

        heading = self._draw_header()
        print(f"{self.table_color}{'=' * self._max_width()}{Color.color_terminate}")
        print(heading)
        print(f"{self.table_color}{'=' * self._max_width()}{Color.color_terminate}")

        self._draw_row(data=data)
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

        def _position_row(new_row=row):
            if position:
                self.data_instance.data.insert(position, new_row)
            else:
                self.data_instance.data.insert(len(self.data_instance.data), new_row)

        new_row_length = len(row)
        table_column_length = len(self.data_instance.data[0])

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

    def _column_exist(self, column):
        # Checks if column to be altered exists
        # and returns True otherwise False
        if column in self.headers:
            self.filter_column = column
            self.data_instance.filter_column = column
            return True

        print(f"Column {column} does not exist")
        return False

    def update(self, column):
        """
        Specifies the table column to update.

        Args:
            Column (String): Column to be updated.

        Returns:
            Table | None
        """
        column_exist = self._column_exist(column)
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
        filter_column_index = self.headers.index(self.filter_column)

        for row in self.data_instance.data:
            if str(row[filter_column_index]) == str(value):
                row[filter_column_index] = updated_value

    def query(self):
        """
        Opens up the table for querying/filtering.

        Returns:
            Data
        """
        return deepcopy(self.data_instance)

    def get_data(self):
        """
        Returns current state of table data

        Returns:
            List
        """
        return self.data_instance.data
