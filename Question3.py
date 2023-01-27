# Generator function to yield next prime number till the iteration value
def total_prime_num(iterator_num):
    inz = 2
    count_prime = 0
    while count_prime < iterator_num:
        # Function to check whether the given number is prime or not
        if num_is_prime(inz):
            # Yield to return the next prime number on each iteration
            yield inz
            # if prime increment the count by 1
            count_prime += 1
        inz += 1

# Function to check whether the given number is prime or not
def num_is_prime(inz):
    if inz < 2:
        return False
    for i in range(2, inz):
        if inz % i == 0:
            return False
    return True

# List to store the prime numbers.
output = []
# Variable to store the total number of iteration to perform.
iteration_value = int(input());
for prime in total_prime_num(iteration_value):
    output.append(prime)

print(output)
