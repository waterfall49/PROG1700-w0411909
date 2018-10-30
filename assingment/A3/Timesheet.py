
def Time_sheet():

    # input    
    day_hours = []
    i=1
    while i <= 5 :
        hours = int(input(f"Enter hours worked on Day #{i}: "))
        day_hours.append(hours)   
        i = i + 1
    print("------------------------------------------------------------")    

    # max day and hours 
    print("The most hours worked was on:")
    max_hour = max(day_hours)
    for c, h in enumerate(day_hours) : 
        if h == max_hour : 
            print(f"Day #{c+1} when you worked {h} hours.") 
    print("------------------------------------------------------------")  

    # total hours and average
    total_hour = sum(day_hours)
    average_hour = total_hour / len(day_hours)
    print(f"The total number of hours worked was : {total_hour} ")
    print(f"The average number of hours worked each day was : {average_hour} ")
    print("------------------------------------------------------------")  

    # slacked off 
    print("Days you slacked off (i.e) worked less than 7 hours) : ")
    for c, h in enumerate(day_hours) : 
        if h < 7 :
            print(f"Day #{c+1}: {h} hours")
    
Time_sheet()
