"""
Assignment Title

Assignment Description

Name..: HYEJUNG BAE
ID....: w0411909
"""

_AUTHOR_ = "Student Name <w0411909@nscc.ca>"

def main():

    # Possible letter grades are A, B, C, D, and F
    # Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above. 
    # Possible modifiers are a plus (+), a minus (–) or nothing. 
    # There is no F+ or F–. 
    # Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3
    # A valid letter grade can be either uppercase or lowercase.
    # If an invalid value is entered, display a warning message                

    print("Grade Point Calculator")
    
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0. ")
    
    # input 
    grade = input("Please enter a letter grade: ")
    grade = grade.upper()
    modifier = input("Please enter a modifier(+,- or nothing): ")

    # process

    modifyingnumber = 0.3

    if grade == "A":
        value = 4
        if modifier == "+":
            totalvalue = value
        elif modifier == "-":
            totalvalue = value - modifyingnumber
        else:
            totalvalue = value
    elif grade == "B":
        value = 3
        if modifier == "+":
            totalvalue = value + modifyingnumber
        elif modifier == "-":
            totalvalue = value - modifyingnumber
        else:
            totalvalue = value        
    elif grade == "C":
        value = 2
        if modifier == "+":
            totalvalue = value + modifyingnumber
        elif modifier == "-":
            totalvalue = value - modifyingnumber
        else:
            totalvalue = value        
    elif grade == "D":
        value = 1
        if modifier == "+":
            totalvalue = value + modifyingnumber
        elif modifier == "-":
            totalvalue = value - modifyingnumber
        else:
            totalvalue = value               
    elif grade == "F":
        value = 0 
        totalvalue = value   
    else:
        print("You entered an invalid letter grade.")

    # output
    display = "The numeric value is: {:.1f}". format(totalvalue)
    print(display)         


if __name__ == "__main__":
    main()    