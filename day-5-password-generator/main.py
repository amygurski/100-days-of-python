import string
import random

print("Welcome to the PyPassword Generator!")

letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like?\n"))
number_count = int(input("How many numbers would you like?\n"))

random_characters = []

for i in range(letter_count):
  random_characters.append(random.choice(string.ascii_letters))

for i in range(symbol_count):
  random_characters.append(random.choice(string.punctuation))

for i in range(number_count):
  random_characters.append(random.choice(string.digits))

shuffled_list = random.sample(random_characters, len(random_characters))
password = ''.join(map(str, shuffled_list))

print(f"Here is your password: {password}")
