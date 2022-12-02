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
    table.draw_table()

    print('\n')

    table.add_row(["Mamba", "Avatar", 32, 43], position=3)
    table.draw_table()

    table.filter("Age").greater_than("30").filter("Count").greater_than("50")
    table.draw_table()