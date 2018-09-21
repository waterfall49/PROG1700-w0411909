"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # input
    earning = input("What is company's earnings per share for the year:")
    price = input("What is price of one share of stock:")

    # process
    ratio = float(price) / float(earning) * 100
    ratio = round(ratio,1)
    
    # output    
    ratio = "company’s price-to-earnings ratio is % "+str(ratio)+" "
    print(ratio)

if __name__ == "__main__":
    main()    