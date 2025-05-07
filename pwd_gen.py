''' This script generates an easy and hard password based on user inputs'''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['@', '%', '&', '*', '(', ')', '^', '#']

print("Welcome to the most Powerful Password Generator\n")
let_len = int(input("How many letters should be included in password?\n"))
num_len = int(input("How many numbers should be included in password?\n"))
sym_len = int(input("How many symbols should be included in password?\n"))

''' -----------  Easy Level  ----------- '''

# password = ""

# for i in range(0, let_len):
#     password += random.choice(letters)

# for i in range(0, num_len):
#     password += random.choice(numbers)

# for i in range(0, sym_len):
#     password += random.choice(symbols)
    
# print(password)

''' -----------  Hard Level  ----------- '''

password = []

for i in range(0, let_len):
    password.append(random.choice(letters))

for i in range(0, num_len):
    password.append(random.choice(numbers))

for i in range(0, sym_len):
    password.append(random.choice(symbols))
    

final_password = ""
for i in range(len(password)):
    final_password += random.choice(password)

print("\nYour Final Password is: ", final_password)