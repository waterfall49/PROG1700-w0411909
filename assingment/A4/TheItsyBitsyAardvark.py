
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

        a = 1
        while a == 1:
            User_Choice = input("Enter Choice(1-5): ")
            if not User_Choice.isnumeric():
                print("Try again. Enter number!")
            elif int(User_Choice) < 1 or int(User_Choice) > 5:
                print("Try to enter the number between 1-5!")
            else: 
                User_Choice = int(User_Choice)
                a += 1

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