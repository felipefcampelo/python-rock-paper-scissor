import random


# Ask the player to choose its option
def play():
    player = input("What's your choice? 'R' for Rock, 'P' for Paper, 'S' for Scissor\n").lower()
    computer = random.choice(['r', 'p', 's'])

    if player == computer:
        return f'''
            You: {choice_name(player)}\n
            Computer: {choice_name(computer)}\n
            It's a tie!
        '''
    elif is_win(player, computer):
        return f'''
            You: {choice_name(player)}\n
            Computer: {choice_name(computer)}\n
            You won!
        '''
    else:
        return f'''
            You: {choice_name(player)}\n
            Computer: {choice_name(computer)}\n
            You lose!
        '''


# r > s, s > p, p > r
def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or \
            (player == 'p' and computer == 'r'):
        return True


def choice_name(choice):
    if choice == 'r':
        return "Rock"
    elif choice == 'p':
        return "Paper"
    else:
        return "Scissor"


match = play()
print(match)
