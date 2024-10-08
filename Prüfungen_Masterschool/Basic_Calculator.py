# Jumps into the Operator of the added user input and Calculates it.
def calculate(text_input):
    # '+' Addition Calculation:
    if '+' in text_input:
        string_list = text_input.split('+')
        return int(string_list[0]) + int(string_list[1])#


    # '-' Subtraction Calculation:
    if '-' in text_input:
        string_list = text_input.split('-')
        return int(string_list[0]) - int(string_list[1])


    # '/' Division Calculation:
    if '/' in text_input:
        string_list = text_input.split('/')
        return int(string_list[0]) / int(string_list[1])


    # '*' Multiplication Calculation:
    if '*' in text_input:
        string_list = text_input.split('*')
        return int(string_list[0]) * int(string_list[1])


    # '*' Reminder Division Calculation:
    if '~' in text_input:
        string_list = text_input.split('~')
        return int(string_list[0]) // int(string_list[1]), int(string_list[0]) % int(
            string_list[1])  # Returns type tuple.


print("Welcome to the Python calculator!")
# Input: Amount calculations
amount_calculations = input("How many calculations do you want to do? ")

# Make amount of calculations from user input requested. Gives output back to user.
for cal in range(int(amount_calculations)):
    user_input = input("What do you want to calculate? ")
    result = calculate(user_input)
    #Checking for type: If '~' was used it will be type 'tuple', cause 2 results will be given back. If not typ 'int' or 'Float'
    if type(result) == tuple:
        print(f"The answer is {result[0]}")
        print(f"The reminder is {result[1]}")
    else:
        print(f"The answer is {result}")
