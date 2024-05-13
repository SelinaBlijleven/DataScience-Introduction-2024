# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.

def print_hello_world():
    print("Hello World!")


def print_hi(name="student"):
    print(f'Hi, {name}')  # Printing in Python with an f-string


def print_student(student):
    if 'name' in student.keys() and 'grade' in student.keys():
        print(f"Student {student['name']} heeft cijfer {student['grade']}")
    else:
        print("Ongeldige data")


# We use this line of code so we do not execute all the
# code every time we import this file.
if __name__ == '__main__':
    print_hello_world()
    print_hi('PyCharm')
    print_hi()
    print_student({'name': "Pietje", "grade": 10})


