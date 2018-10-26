
def main():

    num_list = [  ]

    i = 0
    while i == 0 :
        answer = input("Do you want to continue adding to the list?(yes or no): ")
        answer = answer.lower()
        if answer == "yes" :
            n = 0
            while n == 0 : 
                maybe_num = input("Enter your number: ")
                if not maybe_num.isnumeric(): 
                    print("That is not a numeric! ")
                else : 
                    num = int(maybe_num)
                    num_list.append(num)
                    print(num_list)
                    n = n + 1
        else :
            print("Thank you")
            i = i + 1

    length = len(num_list)
    total = sum(num_list)  
    average = total / length      

    print("The length of number is: " + str(length))    
    print("The sum of numbers is: " +str(total))
    print("The average of numbers is: " +str(average))

main()
