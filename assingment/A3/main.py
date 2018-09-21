"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # input
    watt = input("How much electricity did you spend:")
    hour = input("How many hours did you use:")

    # process
    elect = (watt * hour) / (1000*11.76)
    
    # output    
    electricity = "The cost of the electricity is $ "+str(elect)+" "
    print(electricity)

if __name__ == "__main__":
    main()    