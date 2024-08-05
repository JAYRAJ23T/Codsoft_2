#importing modules ----->>>
from time import *


#introduction !!

print ("WELCOME TO THE TIC TAC TOE")
print ("Made by Jayraj")
print ("______________________________________________")
print ("")
print ("")

#defining the board !!

board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

gamerunning=True #variable to stop and start the game        
winner=None #creating winner variable
chance="X" #first chance of X



 #defining functions to run the game ---->
 
 
  
def game_board(board): #it will print the board !!

   print (" ",board[0] +" | "+ board[1] + " | " + board [2] ," 1 | 2 | 3")
   print (" ","__________"," __________")
   print (" ",board[3] +" | "+ board[4] + " | " + board [5] ," 4 | 5 | 6")
   print (" ","__________"," __________")
   print (" ",board[6] +" | "+ board[7] + " | " + board [8] ," 7 | 8 | 9")
   print ("")
   print ("")
   
   
def player_input(board): # it will take the player input and check if it is alrady not takken !!!
  global chance
  while 0==0 :
   inpt=int(input(f"{chance} enter a number from 1-9 : "))
   print("")
   if inpt >=1 and inpt <= 9 and board[inpt-1] == "_" :
     board[inpt-1] = chance
     break
   else :
     print ("OOPS ! Enter a valid input !!!! ")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     
def horizontal_win (board) : #checking for horizontal wins !!!
  if board [0] == board [1] == board [2] and board [1] != "_" :
    return True
  elif board [3] == board [4] == board [5] and board [4] != "_" :
    return True
  elif board [6] == board [7] == board [8] and board [7] != "_" :
    return True
  else :
    return False
    
def vertical_win (board) : #checking for vertical wins !!
  if board [0] == board [3] == board [6] and board [3] != "_" :
    return True
  elif board [1] == board [4] == board [7] and board [4] != "_" :
    return True
  elif board [2] == board [5] == board [8] and board [5] != "_" :
    return True
  else :
    return False
    
def diagonal_win (board) : #checking for diagonal wins !!
   if board [0] == board [4] == board [8] and board [4] != "_" :
    return True
   elif board [2] == board [4] == board [6] and board [4] != "_":
    return True
   else :
    return False
    
def check_win(board) : # combination of all wins !!
  global winner
  global chance
  if horizontal_win(board) or vertical_win(board) or diagonal_win(board) :
    return True
  else :
    return False

def check_tie(board) : # checking for tie !!
  if "_" not in board :
    return True
  else :
    return False
    
def switch(board) : # switching player !!
  global chance
  
  if chance == "X" :
    chance = "O"
  elif chance == "O" :
    chance = "X"

def replay() : # fuction for replay !!
  global gamerunning 
  global board
  global chance 
  replay = input("do you want to playagain y/n : ")
  if replay == "Y" or replay == "y" :
    gamerunning = True
    board = ["_","_","_",
         "_","_","_",
         "_","_","_"]
    print ("")
    print ("")
    chance = "O"
  elif replay == "N" :
    gamerunning = False 
  else :
    print ("false")

def final() : # combination of all functions to execute the game !!
  global gamerunning 
  while gamerunning :    
   sleep(1)
   game_board(board)    
   player_input(board)
   if check_win(board) :
     game_board(board)
     print (f"CONGRATSSS {chance} WON THE GAME !!")
     gamerunning = False
     replay()
   if check_tie(board) :
     print ("Its a tie !!")
     gamerunning = False
     replay()
   switch(board)
   final()
final()