
def main(): 

    print("The Itsy Bitsy Aardvark\n")
    
    objFile = open("the_choices_file.csv")
    dictLines = {}
    for line in objFile : 
        line = line.replace("\n","")
        listLineContent = line.split(",")
        WordType = listLineContent[0]
        WordChoice = listLineContent[1:]
        dictLines[WordType] = WordChoice

    List_Choices = []

    for choice in dictLines :
        print(f"\nPlease choose {choice}:")
        i = 1
        for words in dictLines[choice] :
            print(f"{i}) {words}")
            i += 1

        User_Choice = 10
        while int(User_Choice) < 1 or int(User_Choice) > 5 or User_Choice.isnumeric() == True :
            User_Choice = input("Enter Choice(1-5): ")  
            if not User_Choice.isnumeric():
                print("Try again. Enter number!")
            else: 
                print("Try to enter the number between 1-5!")
                User_Choice = int(User_Choice)



        # if User_Choice.isnumeric() == True :
        #     User_Choice = int(User_Choice)
        #     while not User_Choice <= 5 : 
        #         User_Choice = int(input("Enter Choice(1-5): "))
        #     else: 
        #         User_Choice = int(User_Choice)
        # else : 
        #     User_Choice = User_Choice
        #     while not User_Choice.isnumeric() :
        #         print("Invalid, Try Agian")
        #         User_Choice = input("Enter Choice(1-5): ")
        #     else : 
        #         User_Choice = int(User_Choice)



        WordChoice = dictLines[choice]
        Choices = WordChoice[User_Choice-1]
        Choices = Choices.upper()
        List_Choices.append(Choices)

    storyFile = open("the_story_file.txt")

    print("\nYour Completed Story: \n")
    for storyFileMsg in storyFile : 
        storyFileMsg = storyFileMsg.replace("\n","")
        for i in range(0,7) :
            strPH = "_"
            strPH += str(i+1)
            strPH += "_"
            storyFileMsg = storyFileMsg.replace(strPH, List_Choices[i])
        print(storyFileMsg)

    objFile.close()        


if __name__ == "__main__":
    main()    