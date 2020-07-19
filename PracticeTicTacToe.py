import pyttsx3

engine = pyttsx3.init("sapi5")
# print(type(engine))
voices = engine.getProperty("voices")
# print(voices[0])
# print(voices[1])
# print(voices[2])

engine.setProperty("voice", voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

board = [" " for i in range(10)]

def printBoard(board):
    print("     |     |     ")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}  ")
    print("     |     |     ")

def spaceIsFree(board, position):
    return board[position] == " "

def insertLetter(board, letter, position):
    board[position] = letter

def isBoardFull(board):
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

def playerMove(board):
    run = True
    while run:
        speak("Please Select A Position To Place An 'X'[1-9] : ")
        move = input("Please Select A Position To Place An 'X'[1-9] : ")
        try:
            move = int(move)
            if move > 0 and move < 10: # if 0 < move < 10
                if spaceIsFree(board, move):
                    run = False
                    insertLetter(board, "X", move)
                else:
                    print("Sorry, This Place Is Occupied")
                    speak("Sorry, This Place Is Occupied")
            else:
                print("Please Type A Number Between 1 And 9")
                speak("Please Type A Number Between 1 And 9")
        except: 
            print("Please Enter A Number")
            speak("Please Enter A Number")

def computerMove(board):
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    # for let in ["0", "X"]:
    #     for i in possibleMoves:
    #         copyBoard = board[:]
    #         copyBoard[i] = let
    #         if winner(copyBoard, let):
    #             move = i
    #             return move

    for i in possibleMoves:
        copyBoard = board[:]
        copyBoard[i] = "0"
        if winner(copyBoard, "0"):
            move = i
            return move   

    for i in possibleMoves:
        copyBoard = board[:]
        copyBoard[i] = "X"
        if winner(copyBoard, "X"):
            move = i
            return move  

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move
    
    edgedOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgedOpen.append(i)

    if len(edgedOpen) > 0:
        move = selectRandom(edgedOpen)
        return move

    return move

def selectRandom(list):
    import random
    length = len(list)
    randomNumber = random.randrange(length)
    return list[randomNumber]

def main():
    print("Welcome To The Game!")
    speak("Welcome To The Game!")
    printBoard(board)
    while not(isBoardFull(board)):
        if not(winner(board, "0")):
            playerMove(board)
            printBoard(board)
        else:
            print("You Loose!")
            speak("You Loose!")
            break
        
        if not(winner(board, "X")):
            move = computerMove(board)
            if move == 0:
                print("Tie Game")
                speak("Tie Game")
            else:
                insertLetter(board, "0", move)
                print("Computer Place An 0 On Position ", move, " :")
                printBoard(board)
                speak(f"Computer Place An 0 On Position {move}")
        else:
            print("You Win!")
            speak("You Win!")
            break
    if isBoardFull(board):
        print("Tie Game")
        speak("Tie Game")

while True:
    main()
    speak("Do You Wan't To Play Again? (yes or no) : ")
    x = input("Do You Wan't To Play Again? (y/n) : ")
    if x.lower() == "y":
        board = [" " for i in range(10)]
        print("------------------------------------------")
        main()
    else:
        speak("Thank You For Playing")
        print("Thank You For Playing")
        break
