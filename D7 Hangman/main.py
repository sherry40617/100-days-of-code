# Hangman

import random
from hangman_stages import stages
from hangman_wordlist import word_list

global display, num, live

gaming = True
life = 6


display = []
chosen_word = random.choice(word_list)
for _ in chosen_word:
    display.append("_")


print("Welcome to Hangman game！")
print("(You can type '?' at anytime to get a missing letter.)\n\n"
             "Let's wait no more and start the game.")
print(f"The word has {len(chosen_word)} letters.\n")


def guess_a_letter(answer):

    global life
    guess = input("Guess a letter: ").lower()
    for letter in range(len(answer)):
        if guess == answer[letter]:
            display[letter] = guess
    def loop():
        global life
        for _ in range(len(chosen_word)):
            num = random.randint(0, len(chosen_word) - 1)
            if guess == "?" and display[num] == "_":
                display[num] = answer[num]
                life -= 1
                print(stages[life])
                break
    loop()

    if (guess not in answer) and (guess != "?"):
        print(f"Oops, {guess} is a wrong letter. You lose a life.")
        life -= 1
        print(stages[life])
    print(" ".join(display))


while gaming:

    guess_a_letter(chosen_word)

    if life == 0:
        print(f"The answer is {chosen_word}.\nYou lose.")
        resume = input("Please type 'Y' to start another round, or type 'N' to quit.").lower()
        if resume == "N":
            gaming = False



    if display.count("_") == 0:
        print("Congrats！You win！")
        resume = input("Please type 'Y' to start another round, or type 'N' to quit.").lower()
        if resume == "N":
            gaming = False




