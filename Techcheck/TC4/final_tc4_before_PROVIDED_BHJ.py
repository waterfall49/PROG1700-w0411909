############################################
# Tech Check 4 - Provided Starter File
############################################

#FUNCTION
def GradeAverageCalculator():

    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

    numericGrade = 0.0

    #letterGrade = input("Please enter a letter grade : ").upper()
    #modifier = input("Please enter a modifier (+, - or nothing) : ")

    # Determine base numeric value of the grade

    subjects = ["PROG1700","NETW1700","OSYS1200","WEBD1000","COMM1700","DBAS1001"]
    
    i=0

    for s in subjects:
        print("Please enter a letter grade for " +s)
        letterGrade = input("").upper()
        modifier = input("Please enter a modifier (+, - or nothing) : \n")

        if letterGrade == "A":
            numericGrade = 4.0
        elif letterGrade == "B":
            numericGrade = 3.0
        elif letterGrade == "C":
            numericGrade = 2.0
        elif letterGrade == "D":
            numericGrade = 1.0
        elif letterGrade == "F":
            numericGrade = 0.0
        else:
            print("You entered an invalid letter grade.")
    
    # Determine whether to apply a modifier

        if modifier == "+":
            if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
                numericGrade += 0.3
        elif modifier == "-":
            if letterGrade != "F":     # Minus is not valid on F
                numericGrade -= 0.3


        if i == 0:
            numericGrade0 = numericGrade
            i = i + 1
        elif i == 1:
            numericGrade1 = numericGrade 
            i = i + 1
        elif i == 2:
            numericGrade2 = numericGrade 
            i = i + 1
        elif i == 3:
            numericGrade3 = numericGrade 
            i = i + 1
        elif i == 4:
            numericGrade4 = numericGrade
            i = i + 1
        elif i == 5:
            numericGrade5 = numericGrade

    print("\nThe numeric value for" +s+ "is: {0:.1f}". format(numericGrade0))
    print("The numeric value for" +s+ "is: {0:.1f}". format(numericGrade1))
    print("The numeric value for" +s+ "is: {0:.1f}". format(numericGrade2))
    print("The numeric value for" +s+ "is: {0:.1f}". format(numericGrade3))
    print("The numeric value for" +s+ "is: {0:.1f}". format(numericGrade4))
    print("The numeric value for" +s+ "is: {0:.1f}". format(numericGrade5))

    average = (numericGrade0+numericGrade1+numericGrade2+numericGrade3+numericGrade4+numericGrade5) / 6
    print("\nYour grade point average for the  semester is: {0:.1f}". format(average))


GradeAverageCalculator()