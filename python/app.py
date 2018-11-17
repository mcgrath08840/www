def create_student():
    #Ask for student name
    student_name = input("Please enter the students name: ")
    grades = input("Please enter students grades: ").split(',')
    #create dictionary in format{'name': "<student_name>', 'marks': []}
    student_dic = {'name': student_name, 'marks': grades}
    #Return dictionary
    return student_dic


def update_student_data(student_dic):
    grades = input("Please enter students grades: ").split(',')
    student_dic['marks'].append(grades)
    print(student_dic)    



update_student_data(create_student())


my_list = []
my_list.append(5)
print(my_list)
