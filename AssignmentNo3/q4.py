def print_student_info(name, roll, age):
    print("Name: {}, Roll: {}, Age: {}".format(name, roll, age))

# Define the data for five students
students = [
    ("John", 101, 20),
    ("Alice", 102, 21),
    ("Bob", 103, 22),
    ("Carol", 104, 23),
    ("David", 105, 24)
]

# Iterate over the list of students and print their information
for student in students:
    print_student_info(*student)
