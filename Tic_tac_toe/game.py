import random
import tictac


board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
#initialized with characters out of scope
excluded_combination=[[4,4]]
#intro and setup
gameover=False
counter=0

print(f"{tictac.toe}\nWelcome to the game. Let's start playing! ")
#assign roles
player_pick=input('Pick if you want to play "X" or "O" by typing it on the console\n').lower()
if player_pick== "x":
    print("You picked X\nThe computer is O")
    computer="O"
elif player_pick == "o":
    print("You picked O\nThe computer is X")
    computer = "X"

#computer move
def computer_move():
    global board, excluded_combination
    row=random.randint(0,2)
    column=random.randint(0,2)
    combination=[row,column]
    if combination not in excluded_combination:
        board[row][column] = computer
        excluded_combination += [[row, column]]
    else:
        computer_move()
    #print(excluded_combination)
    return board, excluded_combination

#make a move
def move():
    global board, excluded_combination
    print(f"This is the board\n{board[0]}\n{board[1]}\n{board[2]}\nWhere do you want to place your move?")
    row=int(input("Which row? (1-3)"))-1
    column=int(input("Which column? (1-3)"))-1
    combination=[row,column]
    if combination not in excluded_combination:
        excluded_combination += [[row, column]]
        board[row][column] = player_pick.upper()

    else:
        print(f"This location on the board is already taken. Please pick another.")
    return board, excluded_combination

def determine_winner(player):
    for x in range(0,2):
        if board[x][0] == player and board[x][1] == player and board[x][2] == player:
            return True
        elif board[0][x] == player and board[1][x] == player and board[2][x] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True


#gameover
while not gameover:
    move()
    counter=+1
    if determine_winner(player=computer):
        gameover=True
        print("You Lose! The winner is the computer")
        print(f"\n{board[0]}\n{board[1]}\n{board[2]}\n")
    elif determine_winner(player=player_pick.upper()):
        gameover=True
        print("Congrats! You are the winner")
        print(f"\n{board[0]}\n{board[1]}\n{board[2]}\n")
    elif counter == 4:
        gameover = True
        print("Game Over! The board is full.")
    else:
        computer_move()

