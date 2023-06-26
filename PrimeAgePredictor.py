import math
from datetime import date

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def next_prime_age_year(birth_year):
    current_year = date.today().year
    age = current_year - birth_year

    while True:
        age += 1
        if is_prime(age):
            return birth_year + age

# Get the user's birth year
birth_year = int(input("Enter your birth year: "))

# Calculate and display the next prime age year
next_year = next_prime_age_year(birth_year)
print("The next year when your age will be a prime number is:", next_year)
input("prompt: ")