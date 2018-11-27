
def Make_Array(File):  # Define function to convert File to 2d-array matrix
    A_Array = []
    for row in File:   
        row = row.replace("\n","")
        row_list = row.split(",")
        A_Array.append(row_list) 
    return(A_Array)

def Input_Validatoin(Entry_Array):  # Define function to validate input value
    a = 1
    while a == 1 :   # to validate input value
        answer = input("\nChoose your target(Ex. A1): ")
        answer = answer.upper()   # not case sensitive 
        if answer == "" or answer[0] == " " or answer[1:] == " " : # Validate for space or enter key
            print("Invalid! Try again")
        elif ord(answer[0]) < 65 or ord(answer[0]) > 74 : # First character should be from A to J
            print("Invalid! Try again")  # If it is integer, it has defferent ASCII code, so it can be checked. 
        elif not answer[1:].isnumeric() : # Second character should be integer.
            print("Invalid! Try again")
        elif int(answer[1:]) < 1 or int(answer[1:]) > 10 : # Second integer character should be between 1 to 10
            print("Invalid! Try again")
        else : 
            X_Row = int(answer[1:])-1   # If first and second character is right, arrange them to new variable
            Y_Column = ord(answer[0])-65
            if Entry_Array[X_Row][Y_Column] == "O" or Entry_Array[X_Row][Y_Column] == "X" : # If I hit same point, should try again! 
                print("You already shot this! Try again!")
            else :
                a = 2
    return(X_Row,Y_Column)

def main():
    
    objFile = open("map.txt")   
    Array = Make_Array(objFile)  # Call the funcation and return the value
    objFile.close()

    print("Let's play Battleship!") 

    scoreGrid = [ [chr(32) for i in range(0,10)] for j in range(0,10) ]  # Make a blank 2d-array matrix 
    success_num = 0  # success number (hit number)
    answerlist_matrix = [] # for finding each battleship
    # below line : ship location (for challenge)
    BS = ((0, 3), (0, 4), (0, 5)), ((1, 8), (2, 8), (3, 8), (4, 8)), ((4, 3), (5, 3)), ((7, 6), (7, 7), (7, 8)),((8, 0), (8, 1), (8, 2), (8, 3), (8, 4))

    for try_num in range(30,0,-1):   # 30 times opportunity
        print(f"You have {try_num} missiles to fire to sink all five ships\n")

        line = (" "*3)   # make an arrange (for printing)
        for i in range(65,75):  # From A to J using ASCII code 
            line += chr(i)
            line += " "
            line = line
        print(line)

        i = 1
        for rows in scoreGrid:   # to arrange for printing 2d array 
            L_letter = ""
            for letter in rows:
                L_letter += str(letter)
                L_letter += " "
            print(f"{i:2d} {L_letter}")
            i += 1 

        X, Y = Input_Validatoin(scoreGrid) # Call the function to validate input and assign return value as new variables

        if Array[X][Y] == "0":
            scoreGrid[X][Y] = "O"  # If I hit non-ship location, save the value with "O" in scoreGrid
            print("Miss")
        else : 
            scoreGrid[X][Y] = "X"  # If I hit ship location, save the value with "X" in scoreGrid
            print("HIT!!!")
            success_num += 1   # for counting success number 

        answerlist_matrix.append((X,Y))  # make a list for finding ship location

        for a in range(0,5):
            if set(BS[a]) <= set(answerlist_matrix) :  # If we hit any of ship perfectly, it shows message
                print(f"You bombed Battle ship {a+1} !!!")

        if success_num == 17 and try_num >= 1 :   # If success number is 17, shows success message, end of game 
            print("YOU SANK MY ENTIRE FLEET!")
            print("You had 17 of 17hits, which sank all the ship")
            print("You won, congraturation!")
            break
        elif success_num < 17 and try_num == 1 :
            print("You have 0 missiles remaining")  # If you hit 30times, shows end message 
            print("GAME OVER")
            print(f"You had {success_num} of 17 hits, but didn't sink all the ship")
            print("Better luck next time.")
            break
        else : 
            continue
    
if __name__ == "__main__":
    main()    
    