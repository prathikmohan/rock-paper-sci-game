import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper or 's' for scissors?\n")
    computer = random.choice(['r','p','s'])
    #print(f'{computer}')

    if user == computer:
        print(f'My choice was also {computer}')
        return 'It\'s a tie :)'
        
    #basic rules of the game is r>s, s>p, p>r
    if is_win(user, computer):
        print(f'My choice was {computer}')
        return 'You win!'
        
    print(f'Ha! My choice was {computer}')
    return 'You lost!!'
    


def is_win(player, opponent):
    #return true if player wins
    #r>s, s>p, p>r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())


