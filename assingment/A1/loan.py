"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # A dollars are borrowed at r% interest compounded weekly to purchase something with weekly payments for n years
    # calculates the weekly payment after the user gives the amount of the loan, interest rate, and number of years

    # input
    loan = float(input("Enter the amount of loan:"))
    rate = float(input("Enter the interest rate(%):"))
    year = float(input("Enter the number of years:"))

    # process
    i = rate / 5200
    m = (1+i)**(-52*year)
    weeklypayment = i / (1-m) * loan
    
    # output    
    weeklypayment = "Your weekly payment will be ${:.2f}".format(weeklypayment)
    print(weeklypayment)

if __name__ == "__main__":
    main()    