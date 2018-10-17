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
    
    for s in subjects:
        print("Please enter a letter grade for " +s)
        letterGrade = input("").upper()
        modifier = input("Please enter a modifier (+, - or nothing) : \n")
        print("The numeric value for" +s+ "is: {0:.1f}". format(numericGrade))

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
        return(numericGrade)
    
    # Determine whether to apply a modifier

        if modifier == "+":
            if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
                numericGrade += 0.3
        elif modifier == "-":
            if letterGrade != "F":     # Minus is not valid on F
                numericGrade -= 0.3
        return(numericGrade)

    for s in subjects:
        print("The numeric value for" +s+ "is: {0:.1f}". format(numericGrade))


GradeAverageCalculator()