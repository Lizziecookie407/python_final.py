# KR EH AT KS 6th Team Game Hangman
import random

#kenji and Adelle
#Variables
words= ["father", "ocean", "water", "kenji", "ducky", "kayze", "eliza", "smoke","train","layer"] 
word = random.choice(words) 

#Kayzee
print(word)
space = "_"
strikes = 0

#Adelle
print("Hi welcome to hangman!\nHow the game consists is we will have a five letter word that will remain unknown, firstly begin to guess a letter to assemble the word, secondly once you guess the letters based on the word a strike will appear if you gain 6 strikes your out, lastly guess the letters to the word and try to complete the word with minimal strikes")

output= f"{space} {space} {space} {space} {space}"
#print(output)

guessed_letters = [0]

#Eliza
def guess():
    user_input = input("Guess a letter: ").strip().lower()
    guessed_letters.append(user_input)
    if user_input in word:
        print(f"Correct!")
        return 0
    else:
        print("Incorrect, guess again.")
        return 1

#Eliza and Kayzee
while strikes < 6:
    strikes += guess()
    print(f"Strikes: {strikes}")
    print(output)
    #for letter in word:
        #if letter in guessed_letters:
            #print(letter)
        #else:
            #print(space)

#Kenji
while strikes == 6:
    print("You lost! Run the code through again.")
    strikes += 1

#Eliza
#for letter in word:
    #if letter in guessed_letters:
    #    print(letter)
    #else:
    #    print(space)

#Kenji and Adelle
if word == user_input:
    print("YOU DID IT!") 
    print(f"{space}")

for letter in word:
    if letter in guessed_letters:
        output.append(letter)
    else:
        output.append(space)

