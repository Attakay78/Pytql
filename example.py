# Example

from pytql import Table, Color, Model, CharField, IntField
from pytql.repl import start_client, ReplType


if __name__ == "__main__":

    class Student(Model):
        first_name = CharField(name="First Name", max_length=20)
        last_name = CharField()
        age = IntField()
        length = IntField()

    class Employee(Model):
        first_name = CharField(name="First Name", max_length=40)
        last_name = CharField(name="Last Name")
        password = CharField()
        city = CharField()

    # Data to populate Student table.
    student_data = [
        ["Richard", "Quaicoe", 23, 243],
        ["Mike", "Kuam", 33, 123],
        ["Roynam", "Skim", 13, 56],
        ["Leon", "Santa", 29, 23],
        ["Geroge"],
    ]

    # Example with passing data with `Student` Model.
    student_table = Table(
        model=Student,
        data=student_data,
        header_color=Color.cyan,
        row_color=Color.green,
        table_color=Color.red,
    )

    # Example with passing file data with `Employee` Model.
    employee_table = Table(
        model=Employee,
        file="user_data.json",
        header_color=Color.cyan,
        row_color=Color.green,
        table_color=Color.blue,
    )
    employee_table.draw_table()

    # Draw student table
    student_table.draw_table()

    # # Add new row to student row at position 3
    # # student_table.add_row(["Jon", "Doe", 23, 232], position=3)
    # # student_table.draw_table(student_table.get_data())

    # # Query student table by filtering `First Name`.
    # t2 = student_table.query().filter_by("First Name").equals("Richard").end_query()
    # student_table.draw_table(t2)

    # # Query student table by filtering with `First Name` and `length` columns.
    t1 = (
        student_table.query()
        .filter_by("First Name")
        .equals("Richard")
        .filter_by("length")
        .greater_than("20")
        .end_query()
    )
    student_table.draw_table(t1)

    # # # Update student `age` column
    student_table.update("age").where("33", "67")
    student_table.draw_table()

    # # # NB: Same operations perform on Student table can be performed on Employee table
    # employee_table.draw_table(employee_table.get_data())
    # start_client(__name__, repl_type=ReplType.ipython_repl)
