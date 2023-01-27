# a decorator that measures the execution time of a function and logs the result to a file
import timeit

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time

        with open("logfile.txt", "a") as f:
            f.write(f"It took {execution_time}s to execute {func.__name__}.\n")

        return result
    return wrapper

@log_execution_time
# function code here
def find_factorial(num):

    factorial = 1

    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i

    return factorial

num = int(input("Enter a number: "))
print("The factorial of",num,"is",find_factorial(num))
