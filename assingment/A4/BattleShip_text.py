
def main():

    objFile = open("map.txt")   

    Array = []
    for row in objFile:   # Convert to objFile to 2d-array matrix
        row = row.replace("\n","")
        row_list = row.split(",")
        Array.append(row_list) 
    objFile.close()

    print("Let's play Battleship!")

    scoreGrid = [ [chr(32) for i in range(0,10)] for j in range(0,10) ]  # Make a blank 2d-array matrix 
    success_num = 0  # succecc number (hit number)

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
                if letter == "," or letter == "[" or letter == "]" :
                    letter = ""
                else : 
                    letter = letter
                L_letter += str(letter)
                L_letter += " "
            print(f"{i:2d} {L_letter}")
            i += 1 

        a = 1
        while a == 1 :   # to validate input value
            answer = input("\nChoose your target(Ex. A1): ")
            answer = answer.upper()
            if answer == "" or answer[0] == " " or answer[1:] == " " :
                print("Invalid! Try again")
            else : 
                X = int(answer[1:])-1   # Change Second charater to be same with index number
                Y = ord(answer[0])-65   # Change first charater to ASCII number, make same with index 
                if X < 0 or X > 9 :    # Second integer character should be between o and 9
                    print("Invalid! Try again")
                elif Y < 0 or Y > 9 :    # If first character should be from A to J
                    print("Invalid! Try again")
                elif scoreGrid[X][Y] == "O" or scoreGrid[X][Y] == "X" : # If I hit same point, should try again! 
                    print("You already shot this! Try again!")
                else :
                    a = 2

        if Array[X][Y] == "0":  
            scoreGrid[X][Y] = "O"  # If I hit non-ship location, save the value with "O" in scoreGrid
            s_num = 0
            print("Miss")
        else : 
            scoreGrid[X][Y] = "X"  # If I hit ship location, save the value with "X" in scoreGrid
            s_num = 1 
            print("HIT!!!")
        
        scoreGrid = scoreGrid  # scoreGrid is accumulated 

        success_num += s_num   # for counting success number 
        if success_num == 17 and try_num >= 1 :   # If success number is 17, shows success message, end of game 
            print("YOU SANK MY ENTIRE FLEET!")
            print("You had 17 of 17hits, which sank all the ship")
            print("You won, congraturation!")
            break
        elif success_num < 17 and try_num == 1 :   # If you hit 30times, shows end message 
            print("You have 0 missiles remaining") 
            print("GAME OVER")
            print(f"You had {success_num} of 17 hits, but didn't sink all the ship")
            print("Better luck next time.")
            break
        else : 
            continue
    
if __name__ == "__main__":
    main()    
    