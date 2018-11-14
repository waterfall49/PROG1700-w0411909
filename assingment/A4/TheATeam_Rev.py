
def strMSG(L_Line,L_Num):
    strMsg = str(L_Num)
    strMsg += ": "
    strMsg += L_Line
    return(strMsg)

def ChangeLetter(L_line):
    if len(L_line) > 20 : 
        L_Line = L_line.lower()
    else : 
        L_Line = L_line.upper()
    return(L_Line) 

def main():

    objFile = open("ateam_Original.txt")
    outFile = open("outFile.txt","w")
    
    print("-"*60)
    print("Original Text")
    print("-"*60)
    print(objFile.read())
    objFile.seek(0)

    Numbered_list = []
    line_number = 1
    for line in objFile : 
        numbered_line = strMSG(line,line_number)
        numbered_line = numbered_line.replace("\n","")
        Numbered_list.append(numbered_line)
        line_number += 1

    CaseChanged_list = []
    for line in Numbered_list : 
        ChangeLine = ChangeLetter(line)
        CaseChanged_list.append(ChangeLine)

    import random
    randomNum = random.randint(1,line_number-1)
    c = 1 
    for o_line in CaseChanged_list :
        if c == randomNum : 
            o_line = " "
            o_line += "\n"
        else :
            o_line = o_line
            o_line += "\n"
        outFile.write(o_line) 
        c += 1

    objFile.close()
    outFile.close()

    outFile = open("outFile.txt")    
    print("-"*60)
    print("Artered Text")
    print("-"*60)
    print(outFile.read())      

    outFile.close()

if __name__ == "__main__":
    main()    