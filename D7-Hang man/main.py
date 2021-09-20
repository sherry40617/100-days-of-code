#Hang Man
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["lion", "dog", "cat", "tiger", "horse", "fish", "sheep", "rabbit"]

import random
chosen_word = random.choice(word_list)
display = []
for a in chosen_word:
  display.append("_")

filled = False
live = 5
while not filled:

  guess = input("Guess a letter: ")
  guess = guess.lower()

  z = 0
  for i in chosen_word:
    if guess == i:
      display[z] = guess
    z += 1
  print(display)


  if guess not in chosen_word:
      print("Oops, it's a wrong letter.")
      print(stages[live])
      if live == 0:
        print("You lose.")
        break
      live -= 1

  if display.count("_") == 0:
      filled = True
      print("You win！")
