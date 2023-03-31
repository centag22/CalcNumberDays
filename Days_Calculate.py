
# programme to calculate number of days in unit of time#
# creating function
def days_unit(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"

# creating function for validation
def validate_and_execute():
    #validate value enter so we use the dictionary key instead of index value in our assigning values#
    try:
        user_input_number = float(days_and_unit_dictionary["days"])

# we want to do conversion only positive numbers
        if user_input_number > 0:
            days_calculations = days_unit(user_input_number, days_and_unit_dictionary["unit"])
            print(days_calculations)

        elif user_input_number == 0:
            print("You entered a 0,Please enter valid day number")
        else:
            print("You entered a negative number,number format does not exist for days")
    except ValueError:
        print("your input is invalid,dont ruin my program")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user,enter a number of days and conversion unit !\n")
# creating variable for user_input.split as(": ")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    # creating dictionary .a dic uses key values , declaring variable with idex to show locations#
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()


