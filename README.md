
# Pytql

Python Table Data Type with some SQL-like operations.


## Authors

- [@AT_Khay (Richard Quaicoe)](https://github.com/Attakay78/)


# API Reference

## Classes

```Class
  Table / Data
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `headers` | `List , Optional` | A collection of table headers | 
| `data` | `List , Optional` | Data to be populated in the table |
| `header_color` | `Color , Optional` | Color for the header |
| `row_color` | `Color , Optional` | Color for the rows |
| `table_color` | `Color , Optional` | Color for the table design |


## Table Methods

```method
  draw_table(data)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `data`    | `List` | **Required**. Table data to be drawn |

**return**:  None


```method
  add_row(data)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `row`    | `List` | **Required**. Row to be added to table | 
| `position`    | `Integer` | Position of the new row |

**return**:  None

```method
  update(column)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `column`    | `String` | **Required**. Column to be updated |

**return**:  Table | None


```method
  where(value, updated_value)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `value`    | `String` |  Current value in table|
| `updated_value`    | `String` |  New value to replace old value|

**return**:  None


```method
  query()
```
**return**:  Data


```method
  get_data()
```
**return**:  List



## Data Methods

```method
  filter_by(column)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `column`    | `String` | **Required**. Column to be filtered |

**return**:  Data | None


```method
  greater_than(value)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `value`    | `String` | **Required**. Value to be filtered by |

**return**:  Data | None


```method
  less_than(value)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `value`    | `String` | **Required**. Value to be filtered by |

**return**:  Data | None


```method
  equals(value)
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `value`    | `String` | **Required**. Value to be filtered by |

**return**:  Data | None


```method
  end_query()
```
**return**:  List
## Installation

Install pytql with pip3

```bash
  pip3 install pytql==[version]
  current version = 0.0.3
```
    
## Usage/Examples

```python
from pytql import Table, Color

if __name__ == '__main__':
    headers = ['First Name', 'Last Name', 'Age', 'Count']

    list_data = [
        ["Richard", "Quaicoe", 23, 243],
        ["Mike", "Kuam", 33, 123],
        ["Roynam", "Skim", 13, 56],
        ["Leon", "Santa", 29, 23],
        ["Geroge"]
    ]

    dict_data = {
        'First Name': ['Richard', 'Mike', 'Roynam', 'Leon', 'George'],
        'Last Name': ['Quaicoe', 'Kuam', 'Skim', 'Santa'],
        'Age': [23, 33, 13, 29],
        'Count': [243, 123, 56, 23]
    }

    # Example with passing dictionary data
    table = Table(data=dict_data, header_color=Color.cyan, row_color=Color.green, table_color=Color.blue)

    # Example with passing list data
    table1 = Table(headers=headers, data=list_data, header_color=Color.cyan, row_color=Color.green, table_color=Color.blue)

    # You can use table (for dict type) or table1 (for list type)
    t_data = table.get_data()
    table.draw_table(t_data)

    table.add_row(["Mamba", "Avatar", 32, 43], position=3)
    table.draw_table(t_data)

    t1 = table.query().filter_by("First Name").equals("Richard").filter_by("Count").greater_than("50").end_query()
    table.draw_table(t1)

    table.update("Age").where("32", "67")
    table.draw_table(t_data)

    t1 = table.query().filter_by("Age").greater_than("50").end_query()
    table.draw_table(t1)

    table.add_row(["Clean", "Quain", 32, 43], position=2)
    table.draw_table(t_data)
```

