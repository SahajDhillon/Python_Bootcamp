# Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
ez_gen = ""
for i in range(1, nr_letters + 1):
    letters_rand = random.choice(letters)
    ez_gen += letters_rand
for i in range(1, nr_numbers + 1):
    numbers_rand = random.choice(numbers)
    ez_gen += numbers_rand
for i in range(1, nr_symbols + 1):
    symbols_rand = random.choice(symbols)
    ez_gen += symbols_rand
print(ez_gen)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_gen = []
password = ""
for j in range(1, nr_letters + 1):
    letters_rand = random.choice(letters)
    hard_gen += letters_rand
for j in range(1, nr_numbers + 1):
    numbers_rand = random.choice(numbers)
    hard_gen += numbers_rand
for j in range(1, nr_symbols + 1):
    symbols_rand = random.choice(symbols)
    hard_gen += symbols_rand
print(hard_gen)
random.shuffle(hard_gen)
k: object
for k in hard_gen:
    password += k
print(password)
