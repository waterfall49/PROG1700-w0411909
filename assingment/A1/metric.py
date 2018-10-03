"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # converts a weight given in tons (imperial), stones, pounds, and ounces 
    # to the metric equivalent in metric tons, kilograms, and grams
    # The number of grams should be displayed to one decimal place

    # input
    tons = int(input("Enter the number of tons:"))
    stone = int(input("Enter the number of stone:"))
    pound = int(input("Enter the number of pounds:"))
    ounce = int(input("Enter the number of ounces:"))

    # process
    totalounce = (35840 * tons) + (224 * stone) + (16 * pound) + ounce
    totalkilos = totalounce / 35.274
    metrictons = int(totalkilos/1000)
    kilos = int(totalkilos % 1000)
    totalgrams = totalkilos * 1000
    grams = totalgrams % (int(totalkilos) * 1000)
    # grams = (totalounce % 35.274) / 35.274 * 1000
    
    # output    
    display ="The metric weight is {0} tons, {1} kilos, and {2:.1f} grams". format(metrictons,kilos,grams) 
    print(display)

if __name__ == "__main__":
    main()    