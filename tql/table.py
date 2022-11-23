class Table:
    def __init__(self, headers=None, data=None):
        self.headers = headers
        self.max_field_widths = []
        self.gap_length = 3
        self.gap = ' '*self.gap_length
        self.data = data


    def _max_width(self):
        total_width = 0
        for width in self.max_field_widths:
            total_width += width
        return total_width + (len(self.max_field_widths) - 1) * self.gap_length
        
        
    def _get_max_field_width(self, column_index):
        row_length = len(self.data)
        
        def _get_max_width(loop_length, mod_type='even'):
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
            return _get_max_width((row_length//2) + 1)


    def draw_header(self):
        format_header = ""
        for index, header in enumerate(self.headers):
            if index == 0:
                format_header += f"{header:{self.max_field_widths[index]}s}"
            else:
                format_header += f"{self.gap}{header:{self.max_field_widths[index]}s}"
        return format_header


    def _draw_row(self):
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

        for column_index in range(len(self.data[0])):
            self.max_field_widths.append(self._get_max_field_width(column_index))

        self.data.pop(0)
 
        heading = self.draw_header()
        print('='*self._max_width())
        print(heading)
        print('='*self._max_width())

        self._draw_row()
    # def add_row(self, row):
    #     """
    #     Add row data to table.

    #     Args:
    #         row (List): Row to be added to table.
        
    #     Returns:
    #         None.
    #     """
    #     if len(self.__table.keys()) == 0:
    #         self.__table_column_size = len(row)
    #         for idx, cell in enumerate(row, 1):
    #             self.__table[f'Column{idx}'] = [cell]
    #     else:
    #         for idx, key in enumerate(self.__table.keys()):
    #             self.__table[key].append(row[idx])


    # def show_table(self):
    #     """
    #     Return table created.

    #     Returns:
    #         __table (dict): Instance of table created.
    #     """
    #     return self.__table
    

    # def add_headers(self, headers):
    #     """
    #     Add header names to table.

    #     Args:
    #         headers (List): Headers to be added to table.
        
    #     Returns:
    #         None
    #     """
    #     if len(self.__table.keys()) == 0:
    #         self.__table_column_size = len(headers)
    #         for header in headers:
    #             self.__table[header] = []
    #     else:
    #         for idx, key in enumerate(self.__table.keys()):
    #             self.__table[headers[idx]] = self.__table.pop(key)
