
def strMSG(L_Line,L_Num): # Define function to make a number of each line
    strMsg = str(L_Num)
    strMsg += ": "
    strMsg += L_Line
    return(strMsg)

def ChangeLetter(L_line): # Define function to change eachline with lower case or upper case 
    if len(L_line) > 20 : 
        L_Line = L_line.lower()
    else : 
        L_Line = L_line.upper()
    return(L_Line) 

def main():

    objFile = open("ateam_Original.txt")  # Open file
    outFile = open("outFile.txt","w")   # Make a new file 
    
    print("-"*60)
    print("Original Text")
    print("-"*60)
    print(objFile.read())
    objFile.seek(0)

    Numbered_list = []
    line_number = 1
    for line in objFile :   # Read each line in objFile 
        numbered_line = strMSG(line,line_number) # call the function to make a number of line, assign new varible for returning 
        numbered_line = numbered_line.replace("\n","") # Replace \n with "" 
        Numbered_list.append(numbered_line) # Append numbered_line to Numbered_list 
        line_number += 1

    CaseChanged_list = []
    for line in Numbered_list : 
        ChangeLine = ChangeLetter(line)  # Call the function to change letter 
        CaseChanged_list.append(ChangeLine)  # Append Changeline to CaseChanged_list 

    import random
    randomNum = random.randint(1,line_number)  # Make random number between 1 to line_number
    c = 1 
    for o_line in CaseChanged_list :  
        if c == randomNum :    # If line number is randon number, delete it
            o_line = " "
            o_line += "\n"
        else :
            o_line = o_line    # If line number is not randon number, don't change
            o_line += "\n"
        outFile.write(o_line)   # Store new line to outfile 
        c += 1

    objFile.close()
    outFile.close()

    outFile = open("outFile.txt")    # Open outfile as reading for printing
    print("-"*60)
    print("Artered Text")
    print("-"*60)
    print(outFile.read())      

    outFile.close()

if __name__ == "__main__":
    main()    