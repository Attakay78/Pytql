# Example

from pytql import Table, Color

if __name__ == "__main__":
    headers = ["First Name", "Last Name", "Age", "Count"]

    list_data = [
        ["Richard", "Quaicoe", 23, 243],
        ["Mike", "Kuam", 33, 123],
        ["Roynam", "Skim", 13, 56],
        ["Leon", "Santa", 29, 23],
        ["Geroge"],
    ]

    dict_data = {
        "First Name": ["Richard", "Mike", "Roynam", "Leon", "George"],
        "Last Name": ["Quaicoe", "Kuam", "Skim", "Santa"],
        "Age": [23, 33, 13, 29],
        "Count": [243, 123, 56, 23],
    }

    # Example with passing dictionary data
    table = Table(
        data=dict_data,
        header_color=Color.cyan,
        row_color=Color.green,
        table_color=Color.blue,
    )

    # Example with passing list data
    table1 = Table(
        headers=headers,
        data=list_data,
        header_color=Color.cyan,
        row_color=Color.green,
        table_color=Color.blue,
    )

    # Example with passing list data (with no headers)
    table2 = Table(
        data=list_data,
        header_color=Color.cyan,
        row_color=Color.green,
        table_color=Color.blue,
    )

    table2.draw_table(table2.get_data())

    table2.add_row(["Jon", "Doe", 23, 232], position=3)
    table2.draw_table(table2.get_data())

    t2 = table2.query().filter_by("Column0").equals("Richard").end_query()
    table2.draw_table(t2)

    # You can use table (for dict type) or table1 (for list type)
    t_data = table.get_data()
    table.draw_table(t_data)

    table.add_row(["Mamba", "Avatar", 32, 43], position=3)
    table.draw_table(t_data)

    t1 = (
        table.query()
        .filter_by("First Name")
        .equals("Richard")
        .filter_by("Count")
        .greater_than("50")
        .end_query()
    )
    table.draw_table(t1)

    table.update("Age").where("32", "67")
    table.draw_table(t_data)

    t1 = table.query().filter_by("Age").greater_than("50").end_query()
    table.draw_table(t1)

    table.add_row(["Clean", "Quain", 32, 43], position=2)
    table.draw_table(t_data)
