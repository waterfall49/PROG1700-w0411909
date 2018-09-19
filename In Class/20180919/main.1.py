"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy_Hyejung Bae <w0411909@nscc.ca>"

def main():
    # input
    item = "Ketchup"
    reg = 1.8
    discount = 0.27    #27%

    #process
    price = reg - reg*discount
    temp = "${0:.2f} is the sale price of {1}"
    disp = temp.format(price,item)

    #output
    print(disp)

if __name__ == "__main__":
    main()    