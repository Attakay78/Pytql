# Example

from table import Table

if __name__ == '__main__':
    headers = ['First Name', 'Last Name', 'Age', 'Count']
    data = [
    ["Richard", "Quaicoe", 23, 243],
    ["Mike", "Kuam", 33, 123],
    ["Roynam", "Skim", 13, 56],
    ["Leon", "Santa", 29, 23],
    # ["Mamba", "Avatar", 32, 43],
    ]

    table = Table(headers=headers, data=data)
    t_data = table.get_data()
    table.draw_table(t_data)

    table.add_row(["Mamba", "Avatar", 32, 43], position=3)
    table.draw_table(t_data)

    t1 = table.query().filter_by("Age").greater_than("30").filter_by("Count").greater_than("50").end_query()
    table.draw_table(t1)

    table.update("Age").where("32", "67")
    table.draw_table(t_data)

    t1 = table.query().filter_by("Age").greater_than("50").end_query()
    table.draw_table(t1)

    table.add_row(["Clean", "Quain", 32, 43], position=2)
    table.draw_table(t_data)
