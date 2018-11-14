
def main(): 

    print("The Itsy Bitsy Aardvark\n")

    strMsg = "Please choose 0 :\n a) 1 \n b) 2 \n c) 3 \n d) 4 \n e) 5 "
    
    inFile = open("the_choices_file.csv")
    inFile = inFile.readlines()
    a = inFile[2]
    print(a)

if __name__ == "__main__":
    main()    