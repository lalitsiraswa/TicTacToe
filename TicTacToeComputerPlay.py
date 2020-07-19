import random

board = [" " for i in range(10)]
# board[0] = "Empty"

def spaceIsFree(position):
    return board[position] == " " 

def insertLetter(letter, position):
    board[position] = letter

def printBoard(board):
    print("     |     |     ")
    print(f"  {board[1]}  |  {board[2]}  |   {board[3]}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board[4]}  |  {board[5]}  |   {board[6]}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board[7]}  |  {board[8]}  |   {board[9]}  ")
    print("     |     |     ")

def isBoardFull(board):
    # return " " in board
    if board.count(" ") > 1:
        return False
    else:
        return True

def winner(board, letter):
    return ((board[1] == board[2] == board[3] == letter) or 
    (board[1] == board[5] == board[9] == letter) or 
    (board[1] == board[4] == board[7] == letter) or
    (board[3] == board[5] == board[7] == letter) or 
    (board[3] == board[6] == board[9] == letter) or 
    (board[4] == board[5] == board[6] == letter) or 
    (board[7] == board[8] == board[9] == letter) or 
    (board[2] == board[5] == board[8] == letter))

def computerMove(board):
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0] # possible = [i for i in range(10)if x[i] == " " and i != 0]
    move = 0

    for let in ["0", "x"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if winner(boardCopy, let):
                move = i
                return move

    if len(possibleMoves) > 1:
        r = random.choice(possibleMoves)
        if r != 0:
            move = r
            return move

    # cornersOpen = []
    # for i in possibleMoves:
    #     if i in [1, 3, 7, 9]:
    #         cornersOpen.append(i)
    
    # if len(cornersOpen) > 0:
    #     move = selectRandom(cornersOpen)
    #     return move

    # if 5 in possibleMoves:
    #     move = 5
    #     return move

    # edgesOpen = []
    # for i in possibleMoves:
    #     if i in [2, 4, 6, 8]:
    #         edgesOpen.append(i)

    # if len(edgesOpen) > 0:
    #     move = selectRandom(edgesOpen)
    #     return move
        
    return move

def selectRandom(list):
    import random
    ln = len(list)
    r = random.randrange(ln)
    return list[r]

def playerMove(board):
    move = input("Please Select A Position To Place An 'X'[1-9] : ")

    try:
        move = int(move)
        if 0 < move < 10:
            if spaceIsFree(move):
                insertLetter("x", move)
            else:
                print("Sorry, This Place Is Occupied")
                playerMove(board)
        else:
            print("Please Type A Number Between 1 Ans 9")
            playerMove(board)
    except:
        print("Please Enter A Number")
        playerMove(board)




    # run = True
    # while run:
    #     move = input("Please Select A Position To Place An 'X'[1-9] : ")
    #     try:
    #         move = int(move)
    #         if move > 0 and move < 10: # if 0 < move < 10
    #             if spaceIsFree(move):
    #                 run = False
    #                 insertLetter("X", move)
    #             else:
    #                 print("Sorry, This Place Is Occupied")
    #         else:
    #             print("Please Type A Number Between 1 Ans 9")
    #     except:
    #         print("Please Enter A Number")



    # validMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # move = int(input("Please Select A Position To Place An 'X'[1-9] : "))
    # if move in validMoves:
    #     if spaceIsFree(move):
    #         board[move] = letter
    #     else:
    #         print("Sorrry This Space Is Occupied")
    #         playerMove()

def main():
    print("Welcome To The Game!")
    printBoard(board)
    while not(isBoardFull(board)):
        if not(winner(board, "0")):
            playerMove(board)
            printBoard(board)
        else:
            print("You Loose!")
            break
        
        if not(winner(board, "X")):
            move = computerMove(board)
            if move == 0:
                print("Tie Game")
            else:
                insertLetter("0", move)
                print("Computer Place An 0 On Position ", move, " :")
                printBoard(board)
        else:
            print("You Win!")
            break
            
while True:
    x = input("Do You Wan't To Play Again? (y/n) : ")
    if x.lower() == "y":
        board = [" " for i in range(10)]
        print("------------------------------------------")
        main()
    else:
        break

        







# def winner(board):
#     if (board[1] == board[2] == board[3] != " "):
#         printBoard(board)
#         print("\nGame Over.\n")                
#         print(" **** " + board[1] + " won. ****")
#     if (board[1] == board[5] == board[9] != " "):
#         printBoard(board)
#         print("\nGame Over.\n")                
#         print(" **** " + board[1] + " won. ****")
#     if (board[1] == board[4] == board[7] != " "):
#         printBoard(board)
#         print("\nGame Over.\n")                
#         print(" **** " + board[1] + " won. ****")
#     if (board[3] == board[5] == board[7] != " "):
#         printBoard(board)
#         print("\nGame Over.\n")                
#         print(" **** " + board[3] + " won. ****")
#     if (board[3] == board[6] == board[9] != " "):
#         printBoard(board)
#         print("\nGame Over.\n")                
#         print(" **** " + board[3] + " won. ****")
#     if (board[4] == board[5] == board[6] != " "):
#         printBoard(board)
#         print("\nGame Over.\n")                
#         print(" **** " + board[4] + " won. ****")
#     if (board[7] == board[8] == board[9] != " "):
#         printBoard(board)
#         print("\nGame Over.\n")                
#         print(" **** " + board[7] + " won. ****")
#     if (board[2] == board[5] == board[8] != " "):
#         printBoard(board)
#         print("\nGame Over.\n")                
#         print(" **** " + board[5] + " won. ****")



    # if ((board[1] == board[3] == "X") or (board[1] == board[3] == "0")):
    #     move = 2
    #     return move
    # elif ((board[1] == board[2] == "X") or (board[1] == board[2] == "0")):
    #     move = 3
    #     return move
    # elif ((board[2] == board[3] == "X") or (board[2] == board[3] == "0")):
    #     move = 1
    #     return move

    # elif ((board[1] == board[4] == "X") or (board[1] == board[4] == "0")):
    #     move = 7
    #     return move
    # elif ((board[1] == board[7] == "X") or (board[1] == board[7] == "0")):
    #     move = 4
    #     return move
    # elif ((board[4] == board[7] == "X") or (board[4] == board[7] == "0")):
    #     move = 1
    #     return move

    # elif ((board[1] == board[5] == "X") or (board[1] == board[5] == "0")):
    #     move = 9
    #     return move
    # elif ((board[1] == board[9] == "X") or (board[1] == board[9] == "0")):
    #     move = 5
    #     return move
    # elif ((board[5] == board[9] == "X") or (board[5] == board[9] == "0")):
    #     move = 1
    #     return move

    # elif ((board[3] == board[5] == "X") or (board[3] == board[5] == "0")):
    #     move = 7
    #     return move
    # elif ((board[3] == board[7] == "X") or (board[3] == board[7] == "0")):
    #     move = 5
    #     return move
    # elif ((board[5] == board[7] == "X") or (board[5] == board[7] == "0")):
    #     move = 3
    #     return move

    # elif ((board[3] == board[6] == "X") or (board[3] == board[6] == "0")):
    #     move = 9
    #     return move
    # elif ((board[3] == board[9] == "X") or (board[3] == board[9] == "0")):
    #     move = 6
    #     return move
    # elif ((board[6] == board[9] == "X") or (board[6] == board[9] == "0")):
    #     move = 3
    #     return move

    # elif ((board[2] == board[5] == "X") or (board[2] == board[5] == "0")):
    #     move = 8
    #     return move
    # elif ((board[2] == board[8] == "X") or (board[2] == board[8] == "0")):
    #     move = 5
    #     return move
    # elif ((board[5] == board[8] == "X") or (board[5] == board[8] == "0")):
    #     move = 2
    #     return move

    # elif ((board[4] == board[5] == "X") or (board[4] == board[5] == "0")):
    #     move = 6
    #     return move
    # elif ((board[4] == board[6] == "X") or (board[4] == board[6] == "0")):
    #     move = 5
    #     return move
    # elif ((board[5] == board[6] == "X") or (board[5] == board[6] == "0")):
    #     move = 4
    #     return move

    # elif (board[7] == board[8] == "X") or ((board[7] == board[8] == "0")):
    #     move = 9
    #     return move
    # elif (board[7] == board[9] == "X") or ((board[7] == board[9] == "0")):
    #     move = 8
    #     return move
    # if (board[8] == board[9] == "X") or ((board[8] == board[9] == "0")):
    #     move = 7
    #     return move