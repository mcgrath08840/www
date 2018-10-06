import random
# User can pick 6 numbers


def get_player_numbers():
    number_csv = input("Enter your 6 numbers, separated by commas: ")

    # Now I want to create a set of integers from
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set

# Lottery calculates 6 rndom numbers (between 1 and 20)
def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values


# Then matches the user numbers to the lottery numbers
# Calculate the winnings based on how many numbers the user matched

#print(get_player_numbers())
print(create_lottery_numbers())
