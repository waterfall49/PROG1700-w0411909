
def LoanCalculator():

    Loan = input("Enter the amount of the loan($): ")

    while not Loan.isnumeric():
        print("Enter the valid number")
        Loan = input("Enter the amount of the loan($): ")

    InterestRate = float(input("Enter the interest rate(%): "))
    Interestfloat = InterestRate * 0.01
    NumberOfDays = int(input("Enter number of days until it is due(days): "))

    interestpay = Interestfloat * Loan

    i=1
    while (i<=NumberOfDays): 
        if i=1:
            print(f"{i} - $  {Interestpay:.2f}"  )
        elif i=2:
            interestdaily = Interestpay * Interestfloat
            print(f"{i} - $  {interestdaily:.2f}"  )
        else:
            interestdaily = Interestdaily * Interestfloat
            print(f"{i} - $  {interestdaily:.2f}"  )
        i = i+1

LoanCalculator()
