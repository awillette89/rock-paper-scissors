import random

name = "Julio"
age = "17"
hobby = "fishing"
print(f"My name is {name}, I am {age} years old, and I love {hobby}")

number = random.randint(1, 100)

def check_number(number):
    if number % 2 == 0:
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")

check_number(number)

new_number = 0
def increment_new_number(new_number):
    while new_number <= 10:
        print(new_number)
        new_number += 1        

increment_new_number(new_number)

#TODO: not working
def add_numbers(a, b):
    return a+b

add_numbers(1, 2)