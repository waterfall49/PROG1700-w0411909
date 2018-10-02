"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Student Name <w0411909@nscc.ca>"

def main():

    # Ask user what country they are from and their order total
    # If Canadian, ask which province
    # If outside Canada, they aren't taxed
    # If Canadian, what is the tax rate? ◦AB: 5% GST
                                         # ON, NB, NS: 15% (5% + 10% prov)
                                         # All other: 11% (5% + 6% prov)
    # Tell the user the total with taxes for their order                                     

    country = input("What country are you from: ")
    country = country.upper()
    order = float(input("Enter your amount of order($): "))
    if country == 'CANADA':
        gst = 0.05
        province = input("Which province do you live(AB,ON,NB,NS,other): ")
        province = province.upper()
        if province == 'AB':
            tax = gst
        elif province == 'ON' or 'NB' or 'NS':
            tax = gst + 0.1 
        else:
            tax = gst + 0.06
        totalorder = order + (order * tax)     
        tax = tax*100
        display = "Your tax is {:.1f}%, total amount of order is {}". format(tax,totalorder)
        print(display)
    else:
        print("You don't need to pay tax! Your total amount of order is "+str(order)+" ")

if __name__ == "__main__":
    main()    