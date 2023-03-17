calculation_time_unit = 24
name_time_unit = "hours"

def days_unit(number_of_days):
    print(number_of_days > 0)
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days*calculation_time_unit} {name_time_unit}"
    elif number_of_days == 0:
        return "Number of days should not be zero it must be a positive number"

def validate_and_execute():
    print(user_input)
    try:
        user_input_number = float(user_input)
        days_calculations = days_unit(user_input_number)
        print(days_calculations)
    except:
        print("your input is invalid,dont ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user,enter a number of days to be converted to hours !\n")
    validate_and_execute()





