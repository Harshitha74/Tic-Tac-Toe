#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output

def display_board(board):
    clear_output()  
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    
def player_input():
    choice='wrong'
    while choice not in ['X','O']:
        choice= input('Player1:Do you want to be X or O?')
        if choice not in ['X','O']:
                clear_output()
    if choice=='X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position]=marker
    
import random
def choose_first():
    if random.randint(0,1)==0:
        return 'Player2'
    else:
        return 'Player1'
    
def win_check(board,mark):
    return((board[7]==mark and board[8]==mark and board[9]==mark) or (board[4]==mark and board[5]==mark and board[6]==mark) or 
           (board[1]==mark and board[2]==mark and board[3]==mark) or (board[7]==mark and board[4]==mark and board[1]==mark) or
           (board[8]==mark and board[5]==mark and board[2]==mark) or (board[9]==mark and board[6]==mark and board[3]==mark) or
           (board[7]==mark and board[5]==mark and board[3]==mark) or (board[1]==mark and board[5]==mark and board[9]==mark))

def space_check(board,position):
    return board[position]==' '

def fullboard_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
        
def player_position(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose your next position:(1-9)'))
    return position

def gameon_choice():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input('Are you ready to play? Enter Y or N: ')
        if choice not in ['Y','N']:
            clear_output()
        if choice=='Y':
            return True
        else:
            return False

def replay():
    p=input('Do you want to play again?Y or N')
    return p=='Y'

print('Welcome to Tic Tac Toe!!')

while True:
    theboard=[' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+' will go first.')
    
    game_on=gameon_choice()
    while game_on:
        if turn=='Player1':
            display_board(theboard)
            position=player_position(theboard)
            place_marker(theboard,player1_marker,position)
            display_board(theboard)
            if win_check(theboard,player1_marker):
                display_board(theboard)
                print('Congratulations! '+ player1_marker +' You won the game!')
                game_on=False
            else:
                if fullboard_check(theboard):
                    display(theboard)
                    print('The game is draw!')
                    break
                else:
                    turn='Player2'
        else:
            #player2's turn.
            display_board(theboard)
            position=player_position(theboard)
            place_marker(theboard,player2_marker,position)
            display_board(theboard)
            if win_check(theboard,player2_marker):
                display_board(theboard)
                print('Congratulations! '+ player2_marker + ' You won the game!')
                game_on=False
            else:
                if fullboard_check(theboard):
                    display(theboard)
                    print('The game is draw!')
                    break
                else:
                    turn='Player1'
    if not replay():
        break

