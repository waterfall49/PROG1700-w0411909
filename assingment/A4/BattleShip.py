
def main():


    # dict = { i :[chr(32) for i in range(1,11)] for i in range(1,11)}
    # print(dict)


    
    # for L_line in F_File : 
    # L_line = L_line.replace("\n","")
    # listLine = L_line.split(",")
    # W_Type = listLine[0]
    # W_Choice = listLine[1:]
    # D_Lines[W_Type] = W_Choice

    # Null_Array = [ [ " " for i in range(0,10) ] for j in range(0,10) ]

    # i = 1
    # for row in Null_Array:
    #     row = row.replace("\n","")
    #     print(f"{i:2d} {row}")
    #     i += 1 

    # i = 1
    # for row in Null_Array:
    #     row = row.replace("\n","")
    #     print(f"{i:2d} {row}")
    #     i += 1

    # for r in range(1,11):
    #     print(f"{r:2d}")

    line = (" "*3)
    for i in range(65,75):
        line += chr(i) 
        line += " "
        line = line
    print(line)

    objFile = open("map.txt")

    i = 1
    for row in objFile:
        row = row.replace("\n","")
        print(f"{i:2d} {row}")
        i += 1 

    objFile.close()
    objFile = open("map.txt")

    Array = []
    for row in objFile:
        row = row.replace("\n","")
        row_list = row.split(",")
        Array.append(row_list) 

    # row = int(input("Enter Row: "))
    # column = int(input("Enter Column: "))
    # print(Array[row][column])
    # print(Array)

    answer = input("Enter Target: ")
    list_answer = []
    for A_answer in answer : 
        list_answer.append(A_answer)
    X = int(list_answer[0])
    Y = int(list_answer[1])

    scoreGrid = [ [0 for i in range(0,10)] for j in range(0,10) ]
    # print(scoreGrid)
    # print(Array[X][Y])
    if Array[X][Y] == "0": 
        scoreGrid[X][Y] = "O"
    else :
        scoreGrid[X][Y] = "X"
    
    #print(scoreGrid)


    line = (" "*3)
    for i in range(65,75):
        line += chr(i) 
        line += " "
        line = line
    print(line)

    i = 1
    for rows in scoreGrid:
        #row = row.replace("\n","")
        for letter in rows:
            if letter == "," or letter == "[" or letter == "]" :
                letter = ""
            else : 
                letter = letter
            letter += letter
        print(f"{i:2d} {row}")
        i += 1 

    # i = 1
    # for s_row in scoreGrid:
    #     s_row = s_row.replace(","," ")
    #     s_row = s_row.replace("[","")
    #     s_row = s_row.replace("]","")
    #     print(f"{i:2d} {s_row}")
    #     i += 1 

    objFile.close()

if __name__ == "__main__":
    main()    
    