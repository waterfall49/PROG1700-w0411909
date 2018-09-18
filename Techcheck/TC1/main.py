"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy_HYEJUNG BAE <w0411909@nscc.ca>"

def main():
    # input
    original = input("your original amount of bill is: ")

    # process
    tax = round(float(original)*0.15,2)
    tip = round(float(original)*0.2,2)
    total = original + tax + tip 
    
    # output
    print("your original bill is: "+str(original)+"")
    print("your tax is: "+str(tax)+"")
    print("your tip is: "+str(tip)+"")
    print("your total amount of bill is: "+str(total)+" ")

if __name__ == "__main__":
    main()    