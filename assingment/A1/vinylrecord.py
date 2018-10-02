"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # Delivery is charged at a rate of $15 per kilometer
    # All purchases are subject to a 14% sales tax
    # the input is provided, the program will display the customer's name and three calculated costs: 
      # delivery cost, records cost (plus tax) and total cost

    # input
    name = input("Enter the customer's name: ")
    distance = float(input("Enter the distance in kilometers for delivery: "))
    cost = float(input("Enter the cost of records purchased: "))

    # process
    rateperkilo = 15
    tax = 0.14
    deliverycost = distance * rateperkilo
    purchsecost = cost + (cost * tax)
    totalcost = deliverycost + purchsecost
    
    # output    
    purchasesummary = "Purchase summary for "+str(name)+" "
    deliverycost = "Delivery Cost:${:.2f} ". format(deliverycost)
    purchsecost = "Purchase Cost:${:.2f} ". format(purchsecost)
    totalcost = "Total Cost:${:.2f} ". format(totalcost)
    print(purchasesummary)
    print(deliverycost)
    print(purchsecost)
    print(totalcost)

if __name__ == "__main__":
    main()