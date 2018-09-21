"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # input
    pledge = input("The amount pledged per mile:")
    mile = input("The number of miles :")

    # process
    ratio = float(pledge) / float(mile)
    
    # output    
    amount = "The amount to be paid is $ "+str(ratio)+" "
    print(amount)

if __name__ == "__main__":
    main()    