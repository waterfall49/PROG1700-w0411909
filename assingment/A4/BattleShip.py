
def main():

    objFile = open("map.txt")

    # print(objFile.read())

    # table = [ [ 0 for i in range(6) ] for j in range(6) ]

    row_list = []
    # column_list = []
    for row in objFile:
        row = row.replace("\n","")
        row_list.append(row)
        # c_list = row.split(",")
        # c_list = int(c_list)
        # column_list.append(c_list)

    # print(column_list)
    print(row_list)

if __name__ == "__main__":
    main()    
    