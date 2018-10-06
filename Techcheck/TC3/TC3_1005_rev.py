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

    if grade == "A":
        value = 4
    elif grade == "B":
        value = 3
    elif grade == "C":
        value = 2   
    elif grade == "D":
        value = 1          
    elif grade == "F":
        value = 0  
    else :
        print("You entered an invalid letter grade.")

    modifyingnumber = 0.3
    
    if modifier == "+":
        if grade != "A" and grade != "F":
            totalvalue = value + modifyingnumber
        else :
            totalvalue = value    
    elif modifier == "-":
        if grade != "F":
            totalvalue = value - modifyingnumber
        else : 
            totalvalue = value
    else :
        totalvalue = value        

    # output
    if grade == "A" or grade == "B" or grade == "D" or grade == "D" or grade == "F":
        display = "The numeric value is: {:.1f}". format(totalvalue)
        print(display)         
    else:    


if __name__ == "__main__":
    main()    