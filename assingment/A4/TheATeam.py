
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

    line_number = 1
    for line in objFile : 
        display = strMSG(line,line_number)
        outFile.write(display)
        line_number += 1

    objFile.close()
    outFile.close()

    objFile = open("outFile.txt","r")
    outFile = open("outFile1.txt","w")

    for line in objFile : 
        ChangeLine = ChangeLetter(line)
        outFile.write(ChangeLine)

    objFile.close()
    outFile.close()

    objFile = open("outFile1.txt","r")
    outFile = open("outFile2.txt","w") 

    import random
    randomNum = random.randint(1,line_number-1)
    c = 1 
    for l in objFile :
        if c == randomNum : 
            l = " "
            l += "\n"
        else :
            l = l
        outFile.write(l) 
        c += 1

    objFile.close()
    outFile.close()

    outFile = open("outFile2.txt")    
    print("-"*60)
    print("Artered Text")
    print("-"*60)
    print(outFile.read())      

    outFile.close()

if __name__ == "__main__":
    main()    