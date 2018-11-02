
def HighestCommonDevisor():            

    def getHighestCommonDevisor(): 

        maybe_num1 = "a"
        while not maybe_num1.isnumeric():
            maybe_num1 = input("\nEnter the first number: ")
            if not maybe_num1.isnumeric(): 
                print("ERROR! Enter a valid first number")
        else : 
            num1 = int(maybe_num1)

        maybe_num2 = "a"
        while not maybe_num2.isnumeric():
            maybe_num2 = input("Enter the second number: ")
            if not maybe_num2.isnumeric(): 
                print("ERROR! Enter a valid second number")
        else : 
            num2 = int(maybe_num2)

        def getFactor(n):
            Num_list = []
            for d in range(1,(n+1)) :
                if n % d == 0 :
                    Num_list.append(d)
            return(Num_list)

        Num_list1 = getFactor(num1)
        Num_list2 = getFactor(num2)
   
        Common_Num_List = []
        for a in Num_list1 : 
            if a in Num_list2 :  
                Common_Num_List.append(a)
        Max_CommonNum = max(Common_Num_List)
        print(f"The Highest Common Divisor of {num1} and {num2} is {Max_CommonNum}.")
       
    getHighestCommonDevisor()

    answer = "y"
    while answer == "y" : 
        answer = input("\nWould you like to try again? (y/n): ")
        answer = answer.lower()
        if answer == "y" :
            getHighestCommonDevisor() 
        else : 
            print("\nThank you for using the HCD program\n")
    else : 
        answer == "n"


HighestCommonDevisor()
