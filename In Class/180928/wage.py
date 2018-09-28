"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Student Name <w0411909@nscc.ca>"

def main():
    hour = input("Enter the the number of hours for this week(hr): ")
    pay = input("Enter your payment per hour($/hr): ")
    hour = float(hour)
    pay = float(pay)
    if hour <= 40 :
        wage = hour * pay
        print("Your wage is $"+str(wage)+" ")
    else :
        exceedwage = (hour-40) * pay * 1.5 
        totalwage = (40 * pay) + exceedwage   
        print("Your wage is $"+str(totalwage)+" ")
    print("Thank you")

if __name__ == "__main__":
    main()    