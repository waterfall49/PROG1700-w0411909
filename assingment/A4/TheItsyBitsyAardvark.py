
def main(): 

    print("The Itsy Bitsy Aardvark\n")

    strMsg = "Please choose 0 :\n a) 1 \n b) 2 \n c) 3 \n d) 4 \n e) 5 "
    
    List = []
    inFile = open("the_choices_file.csv")
    inFile = inFile.readlines()
    sentence = inFile[0]
    print(sentence)
    # List.extend(sentence)
    # print(List)

    for i in sentence : 
        while not i == "," :
            i += i  
            List.append(i)
        else : 
            i = ""
        print(i)

    # for i in range(0,6):
    #     strMsg = strMsg.replace(str(i),sentence1[i])

    print(strMsg)

if __name__ == "__main__":
    main()    