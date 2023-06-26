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

while True:
    user_input = input("Enter your birth year (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Thank you. Exiting the program.")
        break

    try:
        birth_year = int(user_input)
        next_year = next_prime_age_year(birth_year)
        print("The next year when your age will be a prime number is:", next_year)
    except ValueError:
        print("Invalid input. Please enter a valid birth year or 'exit' to quit.")
