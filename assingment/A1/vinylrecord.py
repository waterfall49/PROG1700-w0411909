"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # input
    name1 = input("Enter the customer's name:")
    distance = input("Enter the distance in kilometers for delivery:")
    cost = input("Enter the cost of records purchased:")
    name1 = str(name1)
    distance = float(distance)
    cost = float(cost)

    # process
    rateperkilo = 15
    tax = 0.14
    deliverycost = distance * rateperkilo
    purchsecost = cost + (cost * tax)
    totalcost = deliverycost + purchsecost
    
    # output    
    purchasesummary = "Purchase summary for "+str(name1)+" "
    deliverycost = "Delivery Cost:${:.2f}". format(deliverycost)
    purchsecost = "Purchase Cost:${:.2f}". format(purchsecost)
    totalcost = "Total Cost:${:.2f}". format(totalcost)
    print(purchasesummary)
    print(deliverycost)
    print(purchsecost)
    print(totalcost)

if __name__ == "__main__":
    main()    