"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # input
    fmt = "item: {}, regularPrice: {}, discount: {}". format("ketchup",1.80,0.27)
    print(fmt) 

    # process
    regularPrice = 1.80
    discount = 0.27
    saleprice = regularPrice - discount
    
    # output    
    saleprice = " "+str(saleprice)+" is the sale price of ketchup"
    print(saleprice)

if __name__ == "__main__":
    main()    