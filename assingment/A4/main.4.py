
import math

objFile = open("ateam_Original.txt")
outFile = open("outFile.txt","w")

def strMSG(L_Line,L_Num):
    strMsg = "Length("
    strMsg += str(L_Num)
    strMsg += ") : "
    strMsg += L_Line
    return(strMsg)

def omitline(File,Num):
    randomNum = random.randint(1,Num)
    c = 1
    for l in File : 
        if c == randomNum : 
            l = l.remove()
        else :
            l = l 
        c += 1 
    print(l)        

def main():
    line_number = 1
    for line in objFile : 
        line = line.replace("\n","") 
        if len(line) > 20 :
            line = line.lower()
        else : 
            line = line.upper()
        display = strMSG(line,line_number)
        display += "\n"
        outFile.write(display)
        line_number += 1 

    objFile.close()
    outFile.close()

main()