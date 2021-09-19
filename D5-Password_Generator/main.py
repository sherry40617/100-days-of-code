#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

ingredients = []
for letter_times in range(0, nr_letters):
    ingredients.append(random.choice(letters))

for symbols_times in range(0, nr_symbols):
    ingredients.append(random.choice(symbols))

for numbers_times in range(0, nr_numbers):
    ingredients.append(random.choice(numbers))      # random.choice(LIST) == 從LIST裡面隨機選一個value

random.shuffle(ingredients)     # random.shuffle(LIST) == 打亂LIST裡面的value排序
print("".join(ingredients))     # "".join(LIST) == 用""裡面的東西分隔LIST裡的value
