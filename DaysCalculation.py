#programe to calculate unit of time in days#

# Declaring variables

calculation_time_unit = 24
name_time_unit = "hours"

# creating function
def days_unit(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculation_time_unit} {name_time_unit}"
    elif number_of_days == 0:
        return "Number of days should not be zero it must be a positive number"

# creating function for validation
def validate_and_execute():
    try:
        user_input_number = float(num_of_days_element)

# we want to do conversion only positive numbers
        if user_input_number > 0:
            days_calculations = days_unit(user_input_number)
            print(days_calculations)

        elif user_input_number == 0:
            print("You entered a 0,Please enter valid day number")
        else:
            print("You entered a negative number,number format does not exist for days")
    except ValueError:
        print("your input is invalid,dont ruin my program")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user,enter a number of days as a comma separating list and i will convert it to hours !\n")
# creating variable for user_input.split(", ")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))

    print(type(list_of_days))
    print(type(set(list_of_days)))

# using set to handle repetition of numbers
    for num_of_days_element in set(list_of_days):
        validate_and_execute()
