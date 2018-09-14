"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Student Name <w0411909@nscc.ca>"

def main():
    # input 
    length = 20
    width = 10
    height = 10

    # process
    wall1 = length * height * 2
    wall2 = width * height * 2
    sqft = wall1 + wall2
    # sqft2 = 2 * height ( length + width )
    gallons = sqft / 150 

    # output
    displayGallons = str(gallons)
    displayGallons = "You will need "+displayGallons+" gallons"
    print(displayGallons)             


if __name__ == "__main__":
    main()    