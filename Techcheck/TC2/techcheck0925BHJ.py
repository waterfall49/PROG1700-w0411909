"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    print("Tax Withholding Calculator")

    # input
    salary = input("Please inter the full amount of your weekly salary: ")
    dependent = input("How many dependents do you have?:")
    salary = int(salary)
    dependent = int(dependent)

    # process
    provintax = salary * 0.06
    federaltax = salary * 0.25
    dedution = salary * dependent * 0.02 
    withheld = provintax + federaltax - dedution
    pay = salary - withheld
    
    # output    
    
    totalpay = "Provincial Tax Withheld: ${0:.2f} \n Federal Tax Withheld: ${1:.2f} \n Dependent Deduction for 2 dependents: ${2:.2f} \n Total Withheld: ${3:.2f} \n Total Take-Home Pay: ${4:.2f}". format(provintax,federaltax,dedution,withheld,pay)

    print(totalpay)

if __name__ == "__main__":
    main()    