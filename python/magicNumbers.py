
import random

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        return("You got the number right")
    else:
        return("You didn't quite get it")



magic_numbers = [random.randint(0,9), random.randint(0,9)]


def run_progam_x_times(chances):
    for i in range(chances):
        print("This is attemp {}".format(i + 1))
        print(ask_user_and_check_number())
        

attempts = int(input("Enter a number of attempts you want: "))
run_progam_x_times(attempts)