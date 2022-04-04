# Password generator using python


import random 

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),./0123456789'

number = int(input('How many passwords do you want to generate?: '))

length = int(input('Enter length of password: '))

print('Your passwords are: ')
for i in range(number):
    password = ""
    for j in range(length):
        password += random.choice(chars)
    print(password)