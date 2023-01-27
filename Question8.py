# function that handles the ValueError exception that may be raised when trying to convert a string to an integer.
# The function should prompt the user to enter a new string until a valid integer is entered
def is_valid_input():
    while True:
        try:
            # taking input from user
            user_input = input("Enter an integer: ")
            return int(user_input)
        except ValueError:    # exception handling if input from user is other than integer
            print("Invalid input. Please enter a valid integer.")

# Calling the function
print(is_valid_input())
