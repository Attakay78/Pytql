# Base Model

The base model for creating all Table Models. Inherite the base model to create a new Table Model.

!!! tip ""
    <div style="font-size:21px;"> class pytql.model.Model </div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bases: `object`


## Example

```python hl_lines="1"
class Student(Model):
    first_name = CharField(name="First Name", max_length=20)
    last_name = CharField()
    age = IntField()
    length = IntField()
```