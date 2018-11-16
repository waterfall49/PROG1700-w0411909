
def main():

    objFile = open("map.txt")

    Array = []
    for row in objFile:
        row = row.replace("\n","")
        row_list = row.split(",")
        Array.append(row_list) 

    objFile.close()

    print("Let's play Battleship!")

    scoreGrid = [ [chr(32) for i in range(0,10)] for j in range(0,10) ]

    for try_num in range(30,0,-1):
        print(f"You have {try_num} missiles to fire to sink all five ships\n")

        line = (" "*3)
        for i in range(65,75):
            line += chr(i) 
            line += " "
            line = line
        print(line)

        i = 1
        for rows in scoreGrid:
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
        while a == 1 : 
            answer = input("\nChoose your target(Ex. A1): ")
            answer = answer.upper()
            if answer[0].isnumeric():
                print("Invalid! Try again")
            elif ord(answer[0]) < 65 or ord(answer[0]) > 74 :
                print("Invalid! Try again")
            elif not answer[1:].isnumeric() : 
                print("Invalid! Try again")
            elif int(answer[1:]) > 10 : 
                print("Invalid! Try again")
            else : 
                X = int(answer[1:])-1
                Y = ord(answer[0])-65
                a = 2

        if Array[X][Y] == "0":
            #a = chr(9972) 
            scoreGrid[X][Y] = "O"
            print("Miss")
        else :
            #b = chr(128548)    
            scoreGrid[X][Y] = "X"
            print("HIT!!!")
        
        scoreGrid = scoreGrid
    
if __name__ == "__main__":
    main()    
    