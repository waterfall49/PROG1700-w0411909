
objFile = open("ateam_Original.txt")
objFile.seek(4)
strContent = objFile.readline()
print(strContent)
# outFile = open("outFile.txt","w")

# def strMSG(L_Line,L_Num):
#     strMsg = "Length("
#     strMsg += str(L_Num)
#     strMsg += ") : "
#     strMsg += L_Line
#     return(strMsg)

# line_number = 1
# for line in objFile : 
#     # print(line_number)
#     line = line.replace("\n","") 
#     line = line.upper()
#     display = strMSG(line,line_number)
#     display += "\n"
#     outFile.write(display)
#     line_number += 1 

# objFile.close()
# outFile.close()