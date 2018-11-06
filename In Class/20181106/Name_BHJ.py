
name = input("Enter your name: ")
print(f"Hello {name}")

def PrintElite() :
    for i in range(17): 
        print("I'm elite")

number = int(input("Enter the number: "))

def RepeatPrint() : 
    for i in range(17): 
        print("I'm elite")

def PrintWhile() : 
    i = 1 
    while i <= number : 
        print("I'm elite")
        i = i + 1

def AskAnswer() :
    answer = "yes"
    while answer == "yes" : 
        answer = input("Do you want to continue(yes or no): ")
        answer = answer.lower()
        if answer == "yes" :
            print("I'm elite")
        else :
            break
   

def AskNumber():
    
    num_list = []
    for i in range(10): 
        numbers = input(f"Enter the number #{i+1}: ")
        num_list.append(numbers)
    print(num_list)    

    sumnum = sum(num_list)
    average = sumnum / len(num_list)
    maxnum = max(num_list)

