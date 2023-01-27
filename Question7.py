# function that takes a list of numbers and returns the sum of the numbers that are divisible by 3 or 5
def is_divisible(numbers):
    # generator expression to get the sum of numbers divisible by 3 or 5
    return sum(num for num in numbers if num % 3 == 0 or num % 5 == 0)

# calling the function with the list of numbers
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_list = is_divisible(number_list)
print(sum_list)
