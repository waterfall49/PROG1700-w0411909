
def Cookie_Selloff():

    # input
    num_guides = int(input("Enter the number of guides selling cookies: "))
    list_name = []
    list_box = []

    i = 1
    while i <= num_guides : 
        name = input(f"\nEnter the name of guide #{i}: ")
        num_box = int(input(f"Enter the number of boxes sold by {name}: "))
        list_name.append(name)
        list_box.append(num_box)
        i = i + 1

    # average boxed sold 
    average = sum(list_box) / len(list_box)
    print(f"\nThe average number of boxes sold by each guide was {average:.1f} \n") 

    # Give awards depending their accomplishment 
    print("Guide" + " "*(10-(len("Guide"))) + "Prize Won:")
    print("--------------------------------------------------------")
    for n, b in zip(list_name,list_box) : # n is name, b is number of boxes 
        if b == max(list_box) : 
            print(f"{n}" + " "*(10-(len(n))) + "- Trip to Girl Guide Jamboree in Aruba!")  
        elif b > average and b < max(list_box) : 
            print(f"{n}" + " "*(10-(len(n))) + "- Super Seller Budge")  
        elif b >= 1 and b <= average : 
            print(f"{n}" + " "*(10-(len(n))) + "- Left over cookies")  
        else : 
            print(f"{n}" + " "*(10-(len(n))) + "-")  

Cookie_Selloff()
