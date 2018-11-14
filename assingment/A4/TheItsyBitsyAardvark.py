
def main(): 

    print("The Itsy Bitsy Aardvark\n")

    strMsg = "Please choose 0 :\n a) 1 \n b) 2 \n c) 3 \n d) 4 \n e) 5 "
    
    objFile = open("the_choices_file.csv")
    dictLines = {}
    for line in objFile : 
        line = line.replace("\n","")
        listLineContent = line.split(",")
        WordType = listLineContent[0]
        WordChoice = listLineContent[1:]
        dictLines[WordType] = WordChoice
    print(dictLines)


if __name__ == "__main__":
    main()    