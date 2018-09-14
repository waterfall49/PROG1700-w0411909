"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Student Name <w0411909@nscc.ca>"

def main():

    # input
    cups = input("How many cups of coffee would you like to order: ")
    print("You ordered "+cups+" of coffee")

    # process
    preprice = 1.25 * int(cups)
    tax = 0.15
    price = preprice * (1 + tax)

    # ouput
    price = str(price)
    print("The total amount of cost is $ "+price+" ")

if __name__ == "__main__":
    main()    