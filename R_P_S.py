import random

def play():
    user = input("'r' for Rock, 'p' for Paper, 's' for Scissors: ")
    computer = random.choice(['r', 'p', 's'])  
    # print(f"Computer choice is {computer}") 
    # print(f"User choice is {user}")

    if user == computer:
        return "It is a tie"

    # r > s, s > p, p > r 
    if is_Win(user, computer):
        return "Congrats you won"

    return "You Lost"
    

def is_Win(player, opponent):
    # Return true if player wins
    # r > s, s > p, p > r 
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent =='r') or (player == 's' and opponent == 'p'):
        return True


print(play())