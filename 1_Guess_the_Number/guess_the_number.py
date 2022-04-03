# Program where user will guess any random number entered by the computer.

import random

def humanGuess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input("Enter any number between 1 and {}: ".format(x)))

        if guess > random_number:
            print('Sorry... Too high. Try Again!!')
        elif guess < random_number:
            print('Sorry... Too low. Try Again!!')
    
    print('You guessed the number {} correctly'.format(random_number))


def computerGuess(x):
    low = 1
    high = x

    feedback = '' # empty string

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f' Is {guess} too high (H), too low (L) or Correct (C): ').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'The computer has guessed your number {guess} correctly...')

computerGuess(10)
humanGuess(10)