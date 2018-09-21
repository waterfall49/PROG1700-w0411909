"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Cathy _ HYEJUNG BAE <w0411909@nscc.ca>"

def main():

    # input
    month = input("enter a whole number of months :")

    # process
    year = int(month) / 12
    year = int(year)
    month2 = int(month) % 12
    
    # output    
    yearnmonth ="{0} year and {1}month(s)".format(year,month2)
    print(yearnmonth)

if __name__ == "__main__":
    main()    