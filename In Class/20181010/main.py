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
    length = float(input("What is the lenght of walls: "))
    width = float(input("What is the width of walls: "))
    height = float(input("What is the height of walls: "))

    # process

    def multiple(a,b):
        return(a*b)

    def calceil(g):
        return(math.ceil(g))    

    wall1 = multiple(length,height)   
    wall2 = multiple(width,height)
    sqft = (wall1 + wall2) *2   
    #wall1 = int(length) * int(height) * 2
    #wall2 = int(width) * int(height) * 2
    #sqft = wall1 + wall2
    #sqft = 2 * height ( length + width )
    gallons = sqft / 150 
    maxgallons = calceil(gallons)
    #gallons = math.ceil(gallons) 

    # output
    print(f"You will need {maxgallons} gallons")

    #displayGallons = str(gallons)
    #displayGallons = "You will need "+displayGallons+" gallons"
    #print(displayGallons)             


if __name__ == "__main__":
    main()    