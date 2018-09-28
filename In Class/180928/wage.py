"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Student Name <w0411909@nscc.ca>"

def main():
    hour = input("Enter the the number of hours for this week(hr): ")
    pay = input("Enter your payment per hour($): ")
    hour = float(hour)
    pay = float(pay)
    if hour > 40 :
       print("Your luggage exceeds the weight limit(50lbs), $25 surcharge is applied")
    print("Have a nice trip")

if __name__ == "__main__":
    main()    