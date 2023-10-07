# Model Fields

This part of the documentation covers all field classes for defining the Table column types.

## Field
!!! tip ""
    <i style="font-size:18px;"> <span style="color:blue-grey"> class </span> <span style="color:teal">pytql.fields.Field</span>
    <span style="color:blue-grey">(name: str | None = None, nullable: bool = True, unique: bool = False, editable: bool = True, serialize: bool = True)</span>
    </i>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Base class from which other Field classes inherit from.

Parameters:  

* **name** (str | None) - Name of the column field.
* **nullable** (bool) - Option to determine whether the column can be null.
* **unique** (bool) - Option to determine whether the column should be unique.
* **editable** (bool) - Option to determine whether the column should be editable.
* **serialize** (bool) - Option to determine whether the column should be serialized.

<br>



## BooleanField
!!! tip ""
    <i style="font-size:18px;"> <span style="color:blue-grey"> class </span> <span style="color:teal">pytql.fields.BooleanField</span>
    <span style="color:blue-grey">(name: str | None = None, nullable: bool = True, unique: bool = False, editable: bool = True, serialize: bool = True)</span>
    </i>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bases: [Field](#field)<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Class for setting boolean field values for models.

Parameters:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `BooleanField` inherits all its parameters from base class [Field](#field)
.

<br>



## FloatField
!!! tip ""
    <i style="font-size:18px;"> <span style="color:blue-grey"> class </span> <span style="color:teal">pytql.fields.FloatField</span>
    <span style="color:blue-grey">(name: str | None = None, nullable: bool = True, unique: bool = False, editable: bool = True, serialize: bool = True)</span>
    </i>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bases: [Field](#field)<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Class for setting float field values for models.

Parameters:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `FloatField` inherits all its parameters from base class [Field](#field)
.

<br>



## IntField
!!! tip ""
    <i style="font-size:18px;"> <span style="color:blue-grey"> class </span> <span style="color:teal">pytql.fields.IntField</span>
    <span style="color:blue-grey">(name: str | None = None, nullable: bool = True, unique: bool = False, editable: bool = True, serialize: bool = True)</span>
    </i>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bases: [Field](#field)<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Class for setting integer field values for models.

Parameters:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `IntField` inherits all its parameters from base class [Field](#field)
.

<br>




## CharField
!!! tip ""
    <div style="font-size:18px;"> <span style="color:blue-grey"> class </span> <span style="color:teal">pytql.fields.CharField</span>
    <span style="color:blue-grey">(max_length: int = 225, name: str | None = None, nullable: bool = True, unique: bool = False, editable: bool = True, 
    serialize: bool = True, choices: Any | None = None)</span>
    </div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bases: [Field](#field)<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Class for setting chracter field values for models. Accepts a max size of 255 
characters.

Parameters:  

* **max_length** (int) - Maximum length of field value. 
* **choices** (Any | None) - List of choices field values can be selected

<br>




## TextField
!!! tip ""
    <div style="font-size:18px;"> <span style="color:blue-grey"> class </span> <span style="color:teal">pytql.fields.TextField</span>
    <span style="color:blue-grey">(max_length: int = 225, name: str | None = None, nullable: bool = True, unique: bool = False, editable: bool = True, 
    serialize: bool = True, choices: Any | None = None)</span>
    </div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bases: [CharField](#charfield)<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Class for setting chracter field values for models. Accepts a max size of 1024
characters.

Parameters:  

* **max_length** (int) - Maximum length of field value. 
* **choices** (Any | None) - List of choices field values can be selected

<br>
