import random

from matplotlib.pyplot import get
from words import words 
import string

def get_valid_word(words):
    word = random.choice(words) # randomly select a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # What the user has guessed

    lives = 6

    # Getting the user input
    while len(word_letters) > 0 and lives > 0:

        # letters used

        print('You have used these letters: '," ".join(used_letters))

        # What the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1   # take away a life if the word is wrong
                print("Letter is not in the word.")
                print(f'Lives remaining: {lives}')

        elif user_letter in used_letters:
            print('You have already used that character. Try again!!!')
        else:
            print('Invalid Character... Please try again')

    # Gets here when the len(word_letters) == 0 OR when lives == 0
    
    if lives == 0:
        print('Sorry, You died!! The word was: {}'.format(word))
    else:
        print(f'You guessed the correctly. The word is: {word}')



hangman()