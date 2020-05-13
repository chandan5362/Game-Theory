#!/usr/bin/env python
# coding: utf-8

# ## Tic-Tac-Toe game

# In[1]:


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i,j] == 0:
                sys.stdout.write("_    ")
            elif board[i,j] == 1:
                sys.stdout.write("X   ")
            elif board[i,j] == 2:
                sys.stdout.write("O   ")
        print()


# In[2]:


def checkzeros(board):
    count = 0
    for zero in np.nditer(board):
        if zero == 0:
            count+=1
    return count


# In[3]:


def checkResult(board):
    winner = None
    
# Horizontal winner
    for i in range(len(board)):
        if board[i,0] ==board[i,1] and board[i,1]==board[i,2]  and board[i,0] != 0:
            winner =  board[i,0]
        
#vertical winner
    for i in range(len(board)):
        if board[0,i] ==board[1,i] and board[1,i]==board[2,i]  and board[0,i] != 0:
            winner =  board[0,i]
    
# diagonal winner
    if board[0,0] ==board[1,1] and board[1,1]==board[2,2]  and board[0,0] != 0:
            winner =  board[0,0]
    elif board[2,0] ==board[1,1] and board[1,1]==board[0,2]  and board[2,0] != 0:
            winner = board[2,0]
    
    if checkzeros(board) == 0 and winner is None:
        return 0
    else:
        if winner == 2:
            return 10
        elif winner == 1:
            return -10
        else:
            return None


# In[4]:



def minimax(state,depth,isMaximizing):
    
    returnstate = np.copy(state)
    score =  checkResult(returnstate) 
    if score is not None:
        return score,returnstate
    
    if isMaximizing:
        bestscore = neg_inf
        for i in range(3):
            for j in range(3):
                if state[i,j] == 0:
                    state[i,j] = 2
                    nextstate = np.copy(state)
                    scor,nullstate  = minimax(nextstate,depth+1,False)
                    state[i,j] = 0
                    if scor> bestscore:
                        bestscore = scor
                        returnstate = np.copy(nextstate)
        return bestscore,returnstate
        
    else:
        bestscore = inf
        for i in range(3):
            for j in range(3):
                if state[i,j] == 0:
                    state[i,j] = 1
                    nextstate = np.copy(state)
#                     print(nextstate)
                    scor,nullstate  = minimax(nextstate,depth+1,True)
#                     print(nullstate)
                    state[i,j] = 0
                    if scor < bestscore:
                        bestscore = scor
                        returnstate = np.copy(nextstate)
        
        return bestscore,returnstate
        
                    
    
    
        


# In[5]:


import numpy as np
import sys
neg_inf = -9999999999
inf = 9999999999
board = np.zeros((3,3),dtype = int)
print("Initial configuration of board is:-\n")
printBoard(board)

def main():
    k = 0
    global board
    turn =int(input("enter your turn(1st or 2nd)"))
    for i in range(9):
        if (turn+i)&1:                 #its human turn as "X"
            a,b = [int(x) for x in input("enter the row and column: ").split()]
            board[a-1,b-1] = 1
            printBoard(board)
            if checkResult(board) == -10:
                print("Hurrah! you won the game")
                return
        else:
            temp_state = np.copy(board)
            value,nextstate = minimax(temp_state,0,True )
            board= np.copy(nextstate)
            printBoard(board)
            if checkResult(board)== 10:
                print("pc won! you lost the game")
                return
        
        print("---------------------------------------------------------------------------------------------------------------------------------")
    print("it's a tie")
            
            
            
        


# In[ ]:


# %debug
main()


# In[ ]:




