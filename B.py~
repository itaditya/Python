#!/usr/bin/env python
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "\nLet's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
def cheat():
     print ship_row+1
     print ship_col+1
x=4
mp=int(raw_input("Which mode do you want to try\n1:: Multiplayer\t\t2:: Single Player\n"))
n1=n2="X"
if(mp==1):
  x=10
  print "Both of you shall choose your character (A to Z)\n"
  n1=raw_input()
  n2=raw_input()
 


# Everything from here on should goes in for loop!
# Be sure to indent four spaces!
for turn in range(x+1):
     if (turn + 1)%2==0 and mp==1 :
       print n2+" Turn"
     else:
       print n1+" Turn"
     
     guess_row = int(raw_input("Guess Row:"))-1
     guess_col = int(raw_input("Guess Col:"))-1

     if guess_row == ship_row and guess_col == ship_col:
         print "Congratulations! You sunk my battleship!"
         break
     elif (guess_row == ship_row-1 or guess_row == ship_row+1)and (guess_col == ship_col-1 or guess_col == ship_col+1 )or(guess_row == ship_row and (guess_col == ship_col-1 or guess_col == ship_col+1))or(guess_col == ship_col and (guess_row == ship_row-1 or guess_row == ship_row+1)):
         ship_row = random_row(board)
         ship_col = random_col(board)
         while board[ship_row][ship_col] == n1 or board[ship_row][ship_col] == n2 :
           ship_row = random_row(board)
           ship_col = random_col(board)
         print "Whoosh! You were so close to sinking my Battleship but now it has Drifted to \nAnother Place but as a CONSOLATION this turn has been abandoned ! Surprise !!!! "
         turn-=1
       
     elif guess_row == 1201 and guess_col == 1996:
         print "Cheat Code Successfull!\nThe Coordinates of Ship are\n"
         cheat()
     else:
         if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
              print "Oops, that's not even in the ocean."
         elif(board[guess_row][guess_col] == n1 or board[guess_row][guess_col] == n2):
              print "You guessed that one already."
         elif((turn + 1)%2==0 and mp==1):
             print "You missed my battleship!"
             board[guess_row][guess_col] = n2
             print_board(board)
         else:
              print "You missed my battleship!"
              board[guess_row][guess_col] = n1
     
              print_board(board)
     if turn==x:
         print "Game Over"
