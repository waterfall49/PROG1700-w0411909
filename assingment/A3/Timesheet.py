
def main():

    # input    
    day_hours = []
    i=1
    total_hour = 0
    while i <= 5 :
        hours = int(input(f"Enter hours worked on Day #{i}: "))
        day_hours.append(hours)   
        total_hour = total_hour + day_hours[i-1] #for calculating total hours 
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
    average_hour = total_hour / len(day_hours)
    print(f"The total number of hours worked was : {total_hour} ")
    print(f"The average number of hours worked each day was : {average_hour} ")
    print("------------------------------------------------------------")  

    # slacked off 
    print("Days you slaced off (i.e) worked less than 7 hours) : ")
    for c, h in enumerate(day_hours) : 
        if h < 7 :
            print(f"Day #{c+1}: {h} hours")
    
main()
