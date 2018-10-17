
def paintcalculator():

    #Paint Shop Calculator
    #Program to calculate the number of gallons of paint required to paint a room, if provided the room dimensions
    
    #Import the math class, for using ceiling rounding
    import math

    #Declare variable for # of sq. ft. covered by one gallon of paint
    #square_feet_per_gallon = 150

    #Intro messages
    print("Welcome to the Paint Shop!")
    print("This program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")

    #INPUT
    #Get Dimensions of the room
    length = float(input("\nEnter the length of the room, in feet: "))
    width = float(input("Enter the width of the room, in feet: "))
    height = float(input("Enter the height of the room, in feet: "))

    #PROCESSING
    #Calculate the area of the walls

    def totalarea(a,b,c):   # a,b is length and width, C should be a height
        return((a*c*2) + (b*c*2))

    def gallons(f,g):
        return(f/g)    

    def gallonsofpaint(h):
        return(math.ceil(h))

    squrefeetpergallon = 150   

    area = totalarea(length,width,height)
    gallons = gallons(area,squrefeetpergallon)
    paint = gallonsofpaint(gallons)

    print(f"The total wall area of your room is {area} square feet")
    print(f"You will need {paint} gallon(s) of paint. Happy Painting")    


    #totalArea = (length * height * 2) + (width * height * 2)

    #Divide the area by 150 square feet and
    #round number of gallons up to the nearest whole number
    #gallons_of_paint = math.ceil(totalArea / square_feet_per_gallon)

    #OUTPUT - Display number of gallons needed
    #print("\nThe total wall area of your room is " + str(totalArea) + " square feet.")
    #print("You will need " + str(gallons_of_paint) + " gallon(s) of paint. \n\nHappy Painting!")


paintcalculator()














