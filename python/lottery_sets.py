#numbers = "5,16,25,3,4,1"
#print(numbers.split(","))

#user_numbers = input("enter your numbers, separated by commas: ").split(",")

#user_numbers_as_int = []
#for number in user_numbers:
#    user_numbers_as_int.append(int(number))

#List comprehension
#user_numbers_as_int = [int(number) for number in user_numbers]

#print(user_numbers_as_int)
##########################################################

# Sets - removes duplicates
#numbers = set()
#numbers.add(3)

lottery_values = {3, 5, 17, 6}
user_values = {3, 5, 11, 2}

print(lottery_values)
print(user_values)

# Intersection
print(lottery_values.intersection(user_values))

# Set Comprehension


