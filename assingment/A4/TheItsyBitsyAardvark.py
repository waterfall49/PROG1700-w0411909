
def main(): 

    print("The Itsy Bitsy Aardvark\n")
    
    inFile = open("the_choices_file.csv")
    inFile = inFile.readlines()
    a = inFile[2]
    print(a)

if __name__ == "__main__":
    main()    