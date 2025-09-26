# KR EH AT KS 6th Team Game Hangman
import random

#Variables
words= ["father", "ocean", "water", "kenji", "ducky", "kayze", "eliza", "smoke","train","layer"]
word = random.choice(words) 

print(word)
space = "_"

print("Hi welcome to hangman!\nHow the game consists is we will have a five letter word that will remain unknown, we will have the user guess letters to try and put the word together, once the player guesses a letter it will appear in the order it is in the word, you will have 6 strikes")

#print(f"{space} {space} {space} {space} {space}")




#if word == user_input:
#    print("You guessed the word!")
#else:
#    print("Guess again.")

def guess():
    user_input = input("Guess a letter: ").strip().lower()
    for letter in word:
        if user_input == letter:
            print(f"it matches")
            break
        elif user_input != letter:
            print("that is a strike")
        else:
            print("this is the else statement")


guess()
guess()
guess()
guess()
guess()