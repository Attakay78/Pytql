# PyTQL Table

This section contains information about how to create a PyTQL table and beautify it.

## Class

!!! tip ""
    <i style="font-size:18px;"> <span style="color:blue-grey"> class </span> <span style="color:teal">pytql.table.Table</span>
    <span style="color:blue-grey">(model: [Model](model.md), data=None, file=None, header_color, row_color, table_color)</span>
    </i>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Class used to create Table data type.

Parameters:  

* **model** ([Model](model.md)) - Model to be used to validate table data.
* **data** (Any) - Data to be populated in table. Defaults to `None`.
* **file** (str) - File conatining data to be populated. Defaults to `None`.
* **header_color** ([Color](colors.md)) - Table header color. Defaults to `Color.default`.
* **row_color** ([Color](colors.md)) - Table row color. Defaults to `Color.default`.
* **table_color** ([Color](colors.md)) - Table style color. Defaults to `Color.default`.

<br>

## Methods

> add_row(row, position=None)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Adds additional row data to the table at a specified position. <br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Args**: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; row (List) : Row data to be added to table.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; position (int) : Position of the row data to be added.

<br>


> draw_table(data=None)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Method to draw table with data provided. <br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Args**: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; data (List) : Table data to draw.


??? tip

    Don't pass any data when you want to draw the table. <br>
    Only pass data returned from performing queries or any List of data when you want to visualize the data.

<br>


> get_data( )

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Returns current state of table data. <br><br>



> query( )

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Opens up the table for querying/filtering. <br><br>


> update(column)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Specifies the table column to update. <br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Args**: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; column (str) : Column to be updated.  

<br>


> where(value, updated_value)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Specifies which table data to alter. <br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Args**: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; value (str) : Current value in table.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; updated_value (str) : New value to replace old table value.

<br>