import numpy as np
neg_inf = -9999999
inf = 9999999


# Returns neighbouring index
def getNeighbour(key):
    arr = np.array([(1,3,8),(0,2,4),(1,5,13),(0,4,6,9),(1,3,5),(2,4,7,12),(3,7,10),(5,6,11),(0,9,20),(3,8,10,17),(6,9,14),(7,12,16),(5,11,13,19),(2,12,22),(10,15,17),
    (14,16,18),(11,15,19),(9,14,18,20),( 15,17,19,21),(12,16,18,22),(8,17,21),(18,20,22),(13,19,21 )])
    return arr[key]


#check whether a closed mill is formed or not.It returns a boolean value
def closed_mill(state,pos):
    k0 = (state[0] == state[1] and state[1] == state[2] and state[2]) or (state[0] == state[3] and state[3] == state[6] and state[6]) or (state[0] == state[8] and state[8] == state[20] and state[20])
    k1 = (state[0] == state[1] and state[1] == state[2] and state[2])
    k2 = (state[2] == state[13] and state[13] == state[22] and state[22]) or (state[0] == state[1] and state[1] == state[2] and state[2]) or (state[2]==state[5] and state[5]==state[7] and state[7])
    k3 =  (state[0] == state[3] and state[3] == state[6] and state[6]) or (state[3] == state[4] and state[4] == state[5] and state[5]) or (state[3]==state[9] and state[9] == state[17] and state[17])
    k4 = (state[3] == state[4] and state[4] == state[5] and state[5])
    k5 = (state[2] == state[5] and state[5] == state[7] and state[7]) or (state[3] == state[4] and state[4] == state[5] and state[5]) or (state[5]==state[12] and state[12] == state[19] and state[19])
    k6 = (state[0] == state[3] and state[3] == state[6] and state[6]) or (state[6] == state[10] and state[10] == state[14] and state[14])
    k7 = (state[2] == state[5] and state[5] == state[7] and state[7]) or (state[7] == state[11] and state[11] == state[16] and state[16])
    k8 = (state[0] == state[8] and state[8] == state[20] and state[20]) or (state[8] == state[9] and state[9] == state[10] and state[10])
    k9 = (state[3] == state[9] and state[9] == state[17] and state[17]) or (state[8] == state[9] and state[9] == state[10] and state[10])
    k10 =(state[6] == state[10] and state[10] == state[14] and state[14])
    k11 = (state[7] == state[11] and state[11] == state[16] and state[16] )
    k12 = (state[5] == state[12] and state[12] == state[19] and state[19]) or (state[11] == state[12] and state[12] == state[13] and state[13])
    k13 = (state[11] == state[12] and state[12] == state[13] and state[13]) or (state[2] == state[13] and state[13] == state[22] and state[22])
    k14 = (state[14] == state[15] and state[15] == state[16] and state[16]) or (state[14] == state[17] and state[17] == state[20] and state[20]) or (state[6] == state[10] and state[10] == state[14] and state[14])
    k15 = (state[14] == state[15] and state[15] == state[16] and state[16]) or (state[15] == state[18] and state[18] == state[21] and state[21])
    k16 = (state[14] == state[15] and state[15] == state[16] and state[16]) or (state[16] == state[19] and state[19] == state[22] and state[22])
    k17 =(state[14] == state[17] and state[17] == state[20] and state[20]) or (state[17] == state[18] and state[18] == state[19] and state[19]) or (state[3] == state[9] and state[9] == state[17] and state[17])        
    k18 = (state[17] == state[18] and state[18] == state[19] and state[19]) or (state[15] == state[18] and state[18] == state[21] and state[21])
    k19 = (state[16] == state[19] and state[19] == state[22] and state[22]) or (state[17] == state[18] and state[18] == state[19] and state[19]) or (state[5] == state[12] and state[12] == state[19] and state[19])
    k20 = (state[14] == state[17] and state[17] == state[20] and state[20]) or (state[20] == state[21] and state[21] == state[22] and state[22]) or (state[0] == state[8] and state[8] == state[20] and state[20])
    k21 = (state[15] == state[18] and state[18] == state[21] and state[21]) or (state[20] == state[21] and state[21] == state[22] and state[22])
    k22 = (state[2] == state[13] and state[13] == state[22] and state[22]) or (state[20] == state[21] and state[21] == state[22] and state[22]) or (state[16] == state[19] and state[19] == state[22] and state[22])

    res = [k0,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,k21,k22]

    return res[pos]


class evaluate_utility():
    def __init__(self):
        self.evaluate = 0
        self.board = []

# common minimax for all three phases of Nine Men's morris game
def minimax(state,depth,isMax,alpha,beta,isstage1,Heuristic):
    return_utility = evaluate_utility()
    if depth != 0:
        current_utility = evaluate_utility()

        if isMax:
            if isstage1:
                possible_conf = generateAIboardList(movesOfStage1(InvertedBoard(state)))
            else:
                possible_conf = generateAIboardList(possiblestage20r3(InvertedBoard(state)))
            for board_state in possible_conf:
                nextstate = np.copy(board_state)

                current_utility = minimax(nextstate,depth-1,False,alpha,beta,isstage1,Heuristic)
                if current_utility.evaluate > alpha:
                    alpha = current_utility.evaluate
                    return_utility.board = nextstate
                if alpha >= beta:
                    break
            return_utility.evaluate = alpha
        else:
            if isstage1:
                possible_conf = movesOfStage1(state)
            else:
                possible_conf = movesOfStage3(state)

            for board_state in possible_conf:
                nextstate = np.copy(board_state)
                current_utility = minimax(nextstate,depth-1,True,alpha,beta,isstage1,Heuristic)

                if current_utility.evaluate < beta:
                    beta  = current_utility.evaluate
                    return_utility.board = board_state
                if alpha >= beta:
                    break
            return_utility.evaluate = beta

    else:
        if isMax:
            return_utility.evaluate = Heuristic(InvertedBoard(state),isstage1)
        else:
            return_utility = Heuristic(state,isstage1)

    return return_utility

def possiblestage20r3(state,player = 1):
    cont = 0
    for i in range(len(state)):
        if state[i] == player:
            cont+=1

    if cont == 3:
        return movesOfStage3(state, player)
    else:
        return movesOfStage2(state, player)

# function to invert the board to train the AI
def InvertedBoard(state):
    Inv_board = []
    for i in state:
        if i ==  1:
            Inv_board.append(2)
        elif i == 2:
            Inv_board.append(1)
        else:
            Inv_board.append(0)
    return Inv_board


# generate the list of possible board configuration
def generateAIboardList(board_list):
    result = []
    for i in board_list:
        result.append(InvertedBoard(i))
    return result

def movesOfStage1(state):
    board_list = []
    for  i in range(len(state)):
        if state[i] == 0:
            temp = np.copy(state)
            temp[i] = 1
            if closed_mill(temp,i):
                
                board_list = removeMethod(temp,board_list,1)
            else:
                board_list.append(temp)
    return board_list




# generates the possible board configuaration after all the coins are placed on the board
def movesOfStage2(state,player):
    return_list = []
    for i in range(len(state)):
        if state[i] == player: # palyer == 1
            adj_list = getNeighbour(i)
            for j in adj_list:
                if state[j] == 0:
                    temp = np.copy(state)
                    temp[j],temp[i]= player,0

                    if closed_mill(temp,j):
                        return_list = removeMethod(temp,return_list,player)
                    else:
                        return_list.append(temp)

    return return_list



# generates all possible configuartion of the board when any of the player's coin is reduced to to three
def movesOfStage3(state):
    return_list = []
    for i in range(len(state)):
        if state[i] == 1:
            for j in len(state):
                if state[j] == 0:
                    temp = np.copy(state)
                    temp[j] = 1
                    temp[i] = 0

                    if closed_mill(temp,j):
                        return_list = removeMethod(temp,return_list,1)
                    else:
                        return_list.append(temp)

    return return_list



# removes a coin if opponent forms a mill of three coins
def removeMethod(state,board_list,player):
    if player == 1:
        opponent = 2
    else:
        opponent = 1
    for i in range(len(state)):

        if state[i] == opponent:
            if closed_mill(state,i) == False:
                temp = np.copy(state)
                temp[i] = 0
                board_list.append(temp)
            else:
                board_list.append(state)

    return board_list

# return the total number of mill count at a givem configuration of board
def getMillCount(state,player):
    count = 0

    for i in range(len(state)):
        if (state[i] == 0):
            if closed_mill(state, i):
                count += 1
    return count

# check whether given coin can form a mill or not
def possibleMillFormation(position, state, player):
    adjacent_list = getNeighbour(position)

    for i in adjacent_list:
        if (state[i] == player) and (not closed_mill(state,position)):
            return True
    return False

# returns the total number of possible mill formation
def countOfPossibleMill(state,player):
    cnt = 0
    for i in range(len(state)):
        if (state[i] == player):
            adjacent_list = getNeighbour(i)
            for pos in adjacent_list:
                if (player == 1):
                    if (state[pos] == 2):
                        state[i] = 2
                        if closed_mill(state, i):
                            cnt += 1
                        state[i] = player
                else:
                    if (state[pos] == 1 and possibleMillFormation(pos, state, 1)):
                        cnt += 1
    return cnt


# heuristic function
def HeuristicEvaluationFunction(state,isstage1):
    score = 0
    millPlayer1 = getMillCount(state, 1)
    if not isstage1:
        movable = len(possiblestage20r3(state))

    MillsPlayer2 = countOfPossibleMill(state, 2)

    if not isstage1:
        if np.count_nonzero(state==2) <= 2 or movable == 0: # wining configuration
            score = inf
        elif np.count_nonzero(state==1) <= 2:
            score = neg_inf
        else:
            if (np.count_nonzero(state==1) < 4):
                score += 1 * millPlayer1
                score += 2 * MillsPlayer2
            else:
                score += 2 * millPlayer1
                score += 1 * MillsPlayer2
    else:
        if np.count_nonzero(state==2) < 4:
            score += 1 * millPlayer1
            score += 2 * MillsPlayer2
        else:
            score += 2 * millPlayer1
            score += 1 * MillsPlayer2
    return score
         

        




def printBoard(state):
    board = np.copy(state)
    ################################################################################# board orientation
    print("     pos(20)[{}]--------------------------[{}]--------------------pos(22)[{}]".format(board[20],board[21],board[22]))
    print("             |  \                      pos(21)                       /  |")
    print("             |   \                        |                         /   |")
    print("             |    \                       |                        /    |")
    print("             |     \                      |                       /     |")
    print("             |   17[{}]____________pos(18)[{}]__________________19[{}]     |".format(board[17],board[18],board[19]))
    print("             |    pos(17)                 |                    pos(19)  |")
    print("             |      |  \                  |                   /   |     |")
    print("             |      |   \                 |                  /    |     |")
    print("             |      |    \             pos(15)              /     |     |")
    print("             |      |     [{}]------------[{}]-------------[{}]      |     |".format(board[14],board[15],board[16]))
    print("             |      |  pos(14)                            pos(16) |     |")
    print("             |      |      |                               |      |     |")
    print("             |      |      |                               |      |     |")
    print("             |      |      |                               |      |     |")
    print("      pos(8)[{}]----[{}]----[{}]pos(10)               pos(11)[{}]----[{}]---[{}]pos(13)".format(board[8],board[9],board[10],board[11],board[12],board[13]))
    print("             |    pos(9)   |                               |   pos(12)  |")
    print("             |      |      |                               |      |     |")
    print("             |      |      |                               |      |     |")
    print("             |      |      |                               |      |     |")
    print("             |      |pos(6)[{}]----------------------pos(7)[{}]     |     |".format(board[6],board[7]))
    print("             |      |     /                                 \     |     |")
    print("             |      |    /                                   \    |     |")
    print("             |      |   /                                     \   |     |")
    print("             |      |  /                                       \  |     |")
    print("             |pos(3)[{}]_____________pos(4)[{}]______________pos(5)[{}]    |".format(board[3],board[4],board[5]))
    print("             |      /                      |                      \     |")
    print("             |     /                       |                       \    |")
    print("             |    /                        |                        \   |")
    print("             |   /                         |                         \  |")
    print("      pos(0)[{}]---------------------pos(1)[{}]-------------------pos(2)[{}]".format(board[0],board[1],board[2]))
    #####################################################################################


def main(Heuristic):
    
    depth = 2
    board = np.zeros(23,dtype = int)
    print("Initial configuration of Board is= ")
    printBoard(board)
    # print(closed_mill(board))
    print("\n STAGE -> 1\n")
    score = evaluate_utility()
    for i in range(9):
        print("its your turn \nEnter an input( 'as an array say,1,2,3,4.....')")
        src = int(input("source position ="))
        if board[src] == 0:
            board[src] = 1
            # printBoard(board)
            if closed_mill(board,src):
            
                print("Please enter only valid input")
                rm = int(input("Enter the position to remove an item of opponent\n"))
                # print(np.count_nonzero(board == 1))
                if (board[rm] == 2 and closed_mill(board,rm) ==  False) or (closed_mill(board,rm) and np.count_nonzero(board == 1) == 3) :
                    board[rm] = 0

        print("\nNew configuartion of the board after you  entered is =\n")  
        printBoard(board)
        utility = minimax(board,depth,True,neg_inf,inf,True,Heuristic )
        # print(utility.board)
        print("\nNew configuartion of the board after AI  entered is =\n")  
        printBoard(utility.board)
        board = np.copy(utility.board)
        if utility.evaluate == neg_inf:
            print("you lost")
        

    print("\nPHASE ->2\n")

    print("Now you are out of coins, SInce you have entered in phase-2 \n Configuration of the board is")
    while True:
        printBoard(board)

        print("Enter the position of your coin which you want to move(only valid positions are allowed):")
        src = int(input("source index"))
        dest = int(input("Destination index"))
        board[src],board[dest] = board[dest],board[src]
        if closed_mill(board,dest):
            print("Now yur coins have formed mill ,so please enter below the index of opposition coin to remove it from the board")
            pos = int(input("Position of opposition's coin="))
            if board[pos] == 2 :
                if (not closed_mill(board,pos) or (closed_mill(board,pos) and np.count_nonzero(board == 1) == 3)):
                    board[pos] == 0
                    print("You have successfully removed the opponent")

        printBoard(board)
        utility = minimax(board,depth,True,neg_inf,inf,True,Heuristic )
        if utility.evaluate == neg_inf:
            print("You lost the game")
            exit(0)
        else:
            board = utility.board

        
if __name__ == "__main__":
    print("Welcome to Nine Men's Morris Game\n")
    main(HeuristicEvaluationFunction)

