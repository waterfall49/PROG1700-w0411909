
def LoanCalculator():

    Loan = input("Enter the amount of the loan($): ")

    while not Loan.isnumeric():
        print("Enter the valid number")
        Loan = input("Enter the amount of the loan($): ")

    InterestRate = float(input("Enter the interest rate(%): "))
    Interestfloat = InterestRate * 0.01
    NumberOfDays = int(input("Enter number of days until it is due(days): "))

    Interestpay = Interestfloat * float(Loan)

    i=1
    while i<=NumberOfDays:
        if i==1:
            print(f"{i} - $  {Interestpay:.2f}"  )
        elif i==2:
            Interestdaily = Interestpay * Interestfloat
            Interestpay = Interestpay + Interestdaily
            print(f"{i} - $  {Interestpay:.2f}"  )
        else:
            Interestdaily = Interestpay * Interestfloat
            Interestpay = Interestpay + Interestdaily
            print(f"{i} - $  {Interestpay:.2f}"  )
        i = i+1

    print("Total Owing ")

LoanCalculator()
