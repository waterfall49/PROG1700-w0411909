
def dict_word(F_File):     
    D_Lines = {}
    for L_line in F_File : 
        L_line = L_line.replace("\n","")
        listLine = L_line.split(",")
        W_Type = listLine[0]
        W_Choice = listLine[1:]
        D_Lines[W_Type] = W_Choice
    return(D_Lines)    

def ListofChoices(D_Lines): 
    L_Choices = []
    for C_Choice in D_Lines :
        print(f"\nPlease choose {C_Choice}:")
        i = 1
        for W_Words in D_Lines[C_Choice] :
            print(f"{i}) {W_Words}")
            i += 1
        User_Choice = int(input("Enter Choice(1-5): "))
        W_Choice = D_Lines[C_Choice]
        Choices = W_Choice[User_Choice-1]
        L_Choices.append(Choices)
        return(L_Choices)

def main(): 

    print("The Itsy Bitsy Aardvark\n")
    
    objFile = open("the_choices_file.csv")
    dictLines = dict_word(objFile)
    List_Choices = ListofChoices(dictLines)

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