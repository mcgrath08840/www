student_list = []

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def average_mark(self):
        #Add together all student marks as divide by total number of marks.
        number = len(self.marks)
    
        if number == 0:
            return 0


        total = sum(self.marks)
        return total / number

def create_student():
    #Ask for student name
    name = input("Please enter the students name: ")
    
    #create dictionary in format{'name': "<student_name>', 'marks': []}
    student_data = Student(name)

    #Return object
    return student_data


def add_marks(student, mark):
    #Append mark to student dictionary
    student.marks.append(mark)


def print_student_details(student):
    #Print out details
    print("Name: {}".format(student.name))
    print("Grades: {}".format(student.marks))
    print("{} average: {}".format(student.name, student.average_mark()))

def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)

def menu():
    #Add student to student list
    #Add a mark
    #Print a list of students
    #Exit
    selection = input("Enter 'p' to print the student list,"
        "'s' to add a new student,"
        "'a' to add a mark to a student,"
        "or 'q' to quit." )

    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input("Enter the stuent ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_marks(student, new_mark)
    
        selection = input("Enter 'p' to print the student list,"
            "'s' to add a new student,"
            "'a' to add a mark to a student,"
             "or 'q' to quit." )

menu()


