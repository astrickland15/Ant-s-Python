import re

def is_square_taken(board, m):
        if board[m]=="X" or board[m]=="O":
            return True


def get_winner(_board, _turn):
    
    if _board['1'] == _turn and _board['4'] == _turn and _board['7']== _turn\
        or _board['1']== _turn and _board['2']== _turn and _board['3'] == _turn\
        or _board['1']== _turn and _board['5']==_turn and _board['9'] == _turn\
        or _board['2']== _turn and _board['5']==_turn and _board['8'] == _turn\
        or _board['3']== _turn and _board['5']==_turn and _board['7'] == _turn\
        or _board['3']== _turn and _board['6']==_turn and _board['9'] == _turn\
        or _board['4']== _turn and _board['5']==_turn and _board['6'] == _turn\
        or _board['7']== _turn and _board['8']==_turn and _board['9'] == _turn:        
        
            print_board(_board)
            return True


    



def print_board(board):

    print(board['1'] + '|' + board['2'] +    '|' + board['3'] )
    print("-+-+")
    print(board['4'] + '|' + board['5'] +    '|' + board['6'] )
    print("-+-+")
    print(board['7'] + '|' + board['8'] +    '|' + board['9'] ) 




def play_again():
    response=input(("Play again (y/n)? "))
    
    if response=="y":
        main()
    else:
        print("Goodbye.")


    



def main():


    theBoard={'1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '}
    
    move_count=0
    turn="X"
    for i in range(99):
        
        print_board(theBoard)
                
        print("Turn for: ", turn,".  Select a square.")

        move=(input())

        if not re.match("^[1-9]*$", move) or move=="":

                print("Please enter a valid number (1-9)")
                continue


        if  is_square_taken(theBoard, move):
            print("*** Square is taken, please try again ***")
            
            # retry turn (this will be reversed in line 102)
            if turn=="X":

                turn="O"
            else:
                turn="X"
            
            

        else:
            theBoard[move] = turn
            move_count+=1
            
            
        if get_winner(theBoard, turn):
            print(turn, "wins!")
            play_again()
            break

        elif move_count==9:
            print("This is a draw.")
            print_board(theBoard)
            play_again()
            break
            
        if turn=="X":
            turn="O"
        else:
            turn="X"

if __name__ == "__main__":
    main()




        
    




        

            

           

        

    


       


    


            

            
        
        

     


     



       





