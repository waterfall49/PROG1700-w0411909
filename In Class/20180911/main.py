"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Student Name <w0411909@nscc.ca>"

import math

def main():
    # input 
    length = input("What is the lenght of walls: ")
    width = input("What is the width of walls: ")
    height = input("What is the height of walls: ")

    # process
    wall1 = int(length) * int(height) * 2
    wall2 = int(width) * int(height) * 2
    sqft = wall1 + wall2
    # sqft = 2 * height ( length + width )
    gallons = sqft / 150 
    gallons = math.ceil(gallons)

    # output
    displayGallons = str(gallons)
    displayGallons = "You will need "+displayGallons+" gallons"
    print(displayGallons)             


if __name__ == "__main__":
    main()    