"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # input
    name = input("Enter the customer's name:")
    distance = float(input("Enter the distance in kilometers for delivery:"))
    cost = float(input("Enter the cost of records purchased:"))

    # process
    deliverycost = distance * 15
    purchsecost = cost * 1.14
    
    # output    
    yearnmonth ="{0} year and {1}month(s)".format(year,month2)
    print(yearnmonth)

if __name__ == "__main__":
    main()    