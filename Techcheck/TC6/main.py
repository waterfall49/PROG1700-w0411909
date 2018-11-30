
def dict_list(F_File):    # Define function making file to dictionary list
    D_Lines = {}
    for L_line in F_File : 
        L_line = L_line.replace("\n","")
        listLine = L_line.split(",")
        damage = listLine[-1]
        msgList = listLine[0:2]
        D_Lines[damage] = msgList
    return(D_Lines)    

def main():

    ojbFile = open("monster.csv")
    Dict_Dungeon = dict_list(ojbFile)

    print("\nWelcome to the Dungeon Attack application where none shall survive! Simply try to live as long as you can.")
    
    while True : 
        answer_keepgoing = input("Hit any key to continue ('Q' or 'q' to quit): ")
        answer_keepgoing = answer_keepgoing.upper()
        if answer_keepgoing == "Q":
            print("That's it. Retreat in fear and warn your friends!")
            break
        else :
            while True :
                answer_point = input("Please enter your initial hit points(1-200): ")
                if not answer_point.isnumeric():
                    print("You do not listen very well do you? Think you are going to survice this dungeon?")
                    False
                elif int(answer_point) < 1 or int(answer_point) > 200 : 
                    print("You do not listen very well do you? Think you are going to survice this dungeon?")
                    False
                else : 
                    answer_point = int(answer_point)
                    break
            print("="*100)
            while answer_point > 0: 
                for number in Dict_Dungeon:
                    answer_point = answer_point - int(number)
                    print(f"You were attacked by a {Dict_Dungeon[number][0]} with a {Dict_Dungeon[number][1]} attack for {number} damage")
                    if answer_point < 0 : 
                        answer_point = 0
                        print(f"Current hit points: {answer_point}")
                        break
                    else : 
                        answer_point = answer_point
                        print(f"Current hit points: {answer_point}")
            print("That was sad. And brief. At least the elf feels better about himself!!")


if __name__ == "__main__":
    main()    
