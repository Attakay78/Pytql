class Table:
    """
    A class used to create Table data type.
    """

    def __init__(self, headers=None, data=None):
        """
        Parameters
        ----------
        headers: List, Optional
            A collection of table headers.
        data: Union[List,Tuple, Set, Dictionary], Optional
            The data to be populated in the table.
        """

        self.headers = headers 
        self.max_field_widths = []
        self.gap_length = 3
        self.gap = ' '*self.gap_length
        self.data = data
        self.filter_column = None

    def _max_width(self):
        # Calculates the maximum width of the table.

        total_width = 0
        for width in self.max_field_widths:
            total_width += width
        return total_width + (len(self.max_field_widths) - 1) * self.gap_length
        
    def _get_max_field_width(self, column_index):
        # Calculates the maximum width of each field of the table.

        row_length = len(self.data)
        
        def _get_max_width(loop_length, mod_type='even'):
            # Calculates the maximum width for each field column in the table
            # Using 2 pointer tp reduce the number of iterations in the row
            max_width = 0
            for index in range(loop_length):
                if (mod_type == 'odd') and (index == loop_length - 1):
                    last_val_size = len(str(self.data[index][column_index]))
                    max_width = max_width if max_width > last_val_size else last_val_size
                else:
                    left_val_size = len(str(self.data[index][column_index]))
                    right_val_size = len(str(self.data[row_length-index-1][column_index]))
                    max_val = left_val_size if left_val_size > right_val_size else right_val_size
                    max_width = max_width if max_width > max_val else max_val
            
            return max_width
        
        if row_length%2 == 0:
            return _get_max_width(row_length//2)
        else:
            return _get_max_width((row_length//2) + 1, mod_type="odd")

    def draw_header(self):
        # Drawing table header using string formatting
        format_header = ""
        for index, header in enumerate(self.headers):
            if index == 0:
                format_header += f"{header:{self.max_field_widths[index]}s}"
            else:
                format_header += f"{self.gap}{header:{self.max_field_widths[index]}s}"
        return format_header

    def _draw_row(self):
        # Drawing table rows using string formatting
        for row in self.data:
            format_row = ""
            for index, cell in enumerate(row):
                if index == 0:
                    format_row += f"{str(cell):{self.max_field_widths[index]}s}"
                else:
                    format_row += f"{self.gap}{str(cell):{self.max_field_widths[index]}s}"

            print(format_row)
    
    def draw_table(self):
        self.data.insert(0, self.headers)
        self.max_field_widths = []
        for column_index in range(len(self.data[0])):
            self.max_field_widths.append(self._get_max_field_width(column_index))

        self.data.pop(0)
 
        heading = self.draw_header()
        print('='*self._max_width())
        print(heading)
        print('='*self._max_width())

        self._draw_row()
        print('\n')

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
                self.data.insert(position, new_row)
            else:
                self.data.insert(len(self.data), new_row)

        new_row_length = len(row)
        table_column_length = len(self.data[0])

        if new_row_length == table_column_length:
            _position_row()
        elif new_row_length > table_column_length:
            # If new row data column fields is greater than current table fields, 
            # slice away the extra field data
            _position_row(row[:table_column_length])
        else:
            # If new row data fields is less then current table fields, add None
            # to missing field data
            missing_cells = ["None" for _ in range(table_column_length - new_row_length)]
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
    
    def filter(self, column):
        if column in self.headers:
            self.filter_column = column
            return self
        else:
            print(f"Column {column} does not exist")
            return None

    def operation(self, op_type, value):
        filter_column_index = self.headers.index(self.filter_column)
        temp_data = self.data.copy()

        for row in temp_data:
            if op_type == "greater_than":
                if int(row[filter_column_index]) < int(value):
                    self.data.remove(row)
            elif op_type == "less_than":
                if int(row[filter_column_index]) > int(value):
                    self.data.remove(row)
            elif op_type == "equals":
                if int(row[filter_column_index]) != int(value):
                    self.data.remove(row)
            else:
                print("Invalid operation type")
                return None

        return self

    def greater_than(self, value):
        return self.operation("greater_than", value)

    def less_than(self, value):
        return self.operation("less_than", value)

    def equals(self, value):
        return self.operation("equals", value)
    