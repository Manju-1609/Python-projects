from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('--------------')
    print('|   |   |   |')
    print('| '+board[7]+' | '+board[8]+' | '+board[9]+' |')
    print('|___|___|___|')
    print('|   |   |   |')
    print('| '+board[4]+' | '+board[5]+' | '+board[6]+' |')
    print('|___|___|___|')
    print('|   |   |   |')
    print('| '+board[1]+' | '+board[2]+' | '+board[3]+' |')
    print('|   |   |   |')
    print('--------------')

def player_input():
    
    marker=''
    #Keep asking player to choose X or O
    while marker not in ['X','O']:
        marker=input('Player 1: Do you want to be X or O? ')
        player1=marker
        if player1=='X':
            player2='O'
        else:
            player2='X'
    return (player1,player2)

def place_marker(board, marker, position):
    if position in range(1,10):
        board[position]=marker
        return board
    
def win_check(board, mark):
    winning_conditions={1:[1,2,3],2:[4,5,6],3:[7,8,9],4:[1,5,9],5:[3,5,7],6:[1,4,7],7:[2,5,8],9:[3,6,9]}
    board_check=1
    check_list=[]
    while board_check<10:
        if mark==board[board_check]:
            check_list.append(board_check)
        board_check+=1
    for index in winning_conditions.keys():
        if set(winning_conditions[index])<=set(check_list):
            return True
    return False

import random

def choose_first():
    choice_player=random.randint(1,2)
    print(f'Player {choice_player} will go first')
    return choice_player

def space_check(board, position):
    return board[position]==' '

def full_board_check(board): 
    for val in board:
        if val==' ':
            return False
    return True

def player_choice(board):
    position=0
    while position not in range(1,10) or space_check(board,position)==False:
        position=input('Choose your next position(1-9): ')
        if position.isdigit():
            position=int(position)
            if position in range(1,10):
                if space_check(board,position)==True:
                    return position
                    break
                else:
                    print('This position is already occupied :(')
                    continue
def replay():
    choice=''
    while choice not in ['Yes','No']:
        choice=input('Do you want to play again? Enter Yes or No: ')
        if choice=='Yes':
            return True
        elif choice=='No':
            return False
        else:
            pass
print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player1_marker,player2_marker=player_input()
    curr_player=choose_first()
    option=input('Are you ready to play? Enter Yes or No : ')
    fin=0
    #while game_on:
    if option=='Yes':
        
        while full_board_check(board)==False or fin==1:
            
            #Player 1 Turn
            if curr_player==1:
                position=player_choice(board)
                board=place_marker(board, player1_marker, position)
                display_board(board)
                curr_player=2
                
            # Player2's turn.
            if curr_player==2:
                position_2=player_choice(board)
                board=place_marker(board, player2_marker, position_2)
                display_board(board)
                if win_check(board, player1_marker)==True:
                    print('Congratulations! You have won the game,player 1!')
                    break
                elif win_check(board, player2_marker)==True:
                    print('Congratulations! You have won the game,player 2!')
                    break
                else:
                    curr_player=1
                    if full_board_check(board)== True:
                        fin=1
                    continue
        if replay():
            continue
        else:
            break