
def main():

    line = (" "*3)
    for i in range(65,75):
        line += chr(i) 
        line += " "
        line = line
    print(line)

    Null_Array = [ [ " " for i in range(0,10) ] for j in range(0,10) ]

    i = 1
    for row in Null_Array:
        # row = row.replace("\n","")
        print(f"{i:2d} {row}")
        i += 1 

    # i = 1
    # for row in Null_Array:
    #     row = row.replace("\n","")
    #     print(f"{i:2d} {row}")
    #     i += 1

    # for r in range(1,11):
    #     print(f"{r:2d}")
    

    objFile = open("map.txt")

    Array = []
    for row in objFile:
        row = row.replace("\n","")
        row_list = row.split(",")
        Array.append(row_list)

    objFile.close()

if __name__ == "__main__":
    main()    
    