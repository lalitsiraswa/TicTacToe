game_board = {1 : " ", 2 : " ", 3 : " ", 4 : " ", 5 : " ", 6 : " ", 7 : " ", 8 : " ", 9 : " "} 

def print_game_board():
    print("     |     |     ")
    print(f"  {game_board[1]}  |  {game_board[2]}  |   {game_board[3]}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {game_board[4]}  |  {game_board[5]}  |   {game_board[6]}  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print(f"  {game_board[7]}  |  {game_board[8]}  |   {game_board[9]}  ")
    print("     |     |     ")

def playGame():
    turn = "X"
    count = 0
    while(count < 9):
        print_game_board()
        place = int(input(f"Please Select A Position To Place An '{turn}'[1-9] : "))
        if game_board[place] == " ":
            game_board[place] = turn
        else:
            print("That Place Is Already Filled.\nPlease Choose Other Place?")
            continue
        if game_board[1] != " ":
            if(game_board[1] == game_board[2] == game_board[3]):
                print_game_board()
                print("\nGame Over.\n")                
                print("**** " +turn + " won. ****") 
                break
            if(game_board[1] == game_board[5] == game_board[9]):
                print_game_board()
                print("\nGame Over.\n")                
                print("**** " +turn + " won. ****") 
                break
            if(game_board[1] == game_board[4] == game_board[7]):
                print_game_board()
                print("\nGame Over.\n")                
                print("**** " +turn + " won. ****") 
                break
        if game_board[2] != " ":
            if(game_board[2] == game_board[5] == game_board[8]):
                print_game_board()
                print("\nGame Over.\n")                
                print("**** " +turn + " won. ****") 
                break
        if game_board[3] != " ":
            if(game_board[3] == game_board[6] == game_board[9]):
                print_game_board()
                print("\nGame Over.\n")                
                print("**** " +turn + " won. ****") 
                break
            if(game_board[3] == game_board[5] == game_board[7]):
                print_game_board()
                print("\nGame Over.\n")                
                print("**** " +turn + " won. ****") 
                break
        if game_board[4] != " ":
            if(game_board[4] == game_board[5] == game_board[6]):
                print_game_board()
                print("\nGame Over.\n")                
                print("**** " +turn + " won. ****")
                break 
        if game_board[7] != " ":
            if(game_board[7] == game_board[8] == game_board[9]):
                print_game_board()
                print("\nGame Over.\n")                
                print("**** " +turn + " won. ****")
                break 

        if turn == "X":
            turn = "0"
        else:
            turn = "X"
        count = count + 1
 
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
        
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for keys in game_board.keys():
            game_board[keys] = " "
        playGame()
        
        
if __name__ == "__main__":
    print("----------------------------------------")
    print("Welcome To Tic-Tac_Toe !")
    playGame()

