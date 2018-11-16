    dict = { i :[chr(32) for i in range(1,11)] for i in range(1,11)}
    print(dict)
    
    for L_line in F_File : 
    L_line = L_line.replace("\n","")
    listLine = L_line.split(",")
    W_Type = listLine[0]
    W_Choice = listLine[1:]
    D_Lines[W_Type] = W_Choice

    Null_Array = [ [ " " for i in range(0,10) ] for j in range(0,10) ]

    i = 1
    for row in Null_Array:
        row = row.replace("\n","")
        print(f"{i:2d} {row}")
        i += 1 

    i = 1
    for row in Null_Array:
        row = row.replace("\n","")
        print(f"{i:2d} {row}")
        i += 1

    for r in range(1,11):
        print(f"{r:2d}")

    row = int(input("Enter Row: "))
    column = int(input("Enter Column: "))
    print(Array[row][column])
    print(Array)

        objFile = open("map.txt")

    i = 1
    for row in objFile:
        row = row.replace("\n","")
        print(f"{i:2d} {row}")
        i += 1 

    objFile.close()

        for A_answer in answer :
        A_answer += ","

        # if not A_answer.isnumeric():
        #     A_answer = A_answer.upper()
        #     A_answer = ord(A_answer)-65
        # else :    
        #     A_answer = A_answer
        list_answer.append(A_answer)
    # Character = list_answer[0]
    # Number = list_answer[1:]
    # print(list_answer)
    # list_answer.insert(1,",")
    # print(list_answer)