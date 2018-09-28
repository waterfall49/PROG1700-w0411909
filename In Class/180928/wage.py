"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Student Name <w0411909@nscc.ca>"

def main():
    weight = input("Enter the total weight of your luggage(lbs): ")
    weight = float(weight)
    if weight > 50 :
       print("Your luggage exceeds the weight limit(50lbs), $25 surcharge is applied")
    print("Have a nice trip")

if __name__ == "__main__":
    main()    