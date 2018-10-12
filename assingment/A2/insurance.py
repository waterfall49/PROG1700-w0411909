
def autoinsurance():

    # input
    gender = input("Are you 'Male' or 'Female': ")
    gender = gender.lower()
    age = float(input("Enter your age: "))
    price = float(input("Enter the purchase of the vehicle: "))

    # process

    def monthlyrate(a):
        return(a * 0.01 / 12)

    def monthlypayment(b,c):
        return(b*c)

    if gender == "male" :
        if age >= 15 and age < 25 :
            insurancerate = 25
        elif age >= 25 and age < 40 :
            insurancerate = 17
        elif age >= 40 and age < 70 :
            insurancerate = 10
        else:
            insurancerate = 0
    else: 
        if age >= 15 and age < 25 :
            insurancerate = 20
        elif age >= 25 and age < 40 :
            insurancerate = 15
        elif age >= 40 and age < 70 :
            insurancerate = 10
        else:
            insurancerate = 0     

    payment = monthlypayment(monthlyrate(insurancerate),price)

    # output    

    print(f"Your monthly insurance will be ${payment:.2f}")

autoinsurance()
