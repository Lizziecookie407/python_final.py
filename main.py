# KR EH AT KS 6th Team Game Hangman

import random

#Kenji and Adelle
words= ["father","ocean","water","kenji","ducky","kayze","eliza","smoke","train", "layer","alone","brain","craft","paint","flute","beach","heart","human","image","lemon","lucky","mouse","metal","noise","plane","phone","power","quiet","ready","store","sport","storm","today","table","under","video","watch","young"] 
word = random.choice(words)

#Kayzee
#print(word)
space = "_"
strikes = 0

#Adelle
print("Hi welcome to hangman!\nThis game consists of an unkown five letter word. First, begin to assemble the word by guessing one letter at a time. Second, if you guess a letter that is not in the word, a strike will appear. If you gain 6 strikes, you're out. Lastly, guess letters to try to complete the word with minimal strikes. Have fun playing!")

guessed_letters = []
output_list = []

#Eliza and Kayzee
def guess():
    user_input = input("Guess a letter: ").strip().lower()
    if user_input in guessed_letters:
        print("You already guessed that letter!")
        return 0
    else:
        guessed_letters.append(user_input)
    if user_input in word:
        print(f"Correct!")
        return 0
    else:
        print("Incorrect, guess again.")
        return 1

#Eliza
while strikes < 6:
    strikes += guess()
    print(f"Strikes: {strikes}")
    for letter in word:
        if letter in guessed_letters:
            output_list += letter
        else:
            output_list += space
    output = (' '.join(output_list))
    print(output)
    output_list = []
    if ' '.join(word).strip() == output: #Kenji and Adelle
        print("Horray! You guessed the word! Rerun the code to play again.")
        break
    else:
        continue

#Kenji
while strikes == 6:
    print("You lost! Rerun the code to play again.")
    strikes += 1