"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # input
    tons = input("Enter the number of tons:")
    stone = input("Enter the number of stone:")
    pound = input("Enter the number of pounds:")
    ounce = input("Enter the number of ounces:")

    # process
    totalounce = (35840 * tons) + (224 * stone) + (16 * pound) + ounce
    totalkilos = totalounce / 35.274
    metrictons = int(totalkilos/1000)
    kilos = totalkilos % 1000
    grams = totalounce % 35.274
    
    # output    
    display ="The metric weight is {0} tons, {1} kilos, and {2:.1f} grams".format(tons,kilos,grams) 
    print(display)

if __name__ == "__main__":
    main()    