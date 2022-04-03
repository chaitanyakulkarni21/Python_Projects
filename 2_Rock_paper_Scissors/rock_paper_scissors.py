# Rock Paper Scissors


import random


def play():
    user = input("What's your choice?  'R' for Rock, 'S' for Scissors or 'P' for Papers: \n").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie...'

    if isWin(user, computer):
        return 'You Won!!!'
    
    return 'You Lost!!!'


    

'''
Rule: 

Rock beats paper, scissor beats paper and Paper beats rock

r > p, s > p and p > r
'''
def isWin(player, opponent):
    
    if (player == 'r' and opponent == 'p') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True 

print(play())