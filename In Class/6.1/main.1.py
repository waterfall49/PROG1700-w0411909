
def LoanCalculator():

    Loan = input("Enter the amount of the loan($): ")

    while not Loan.isnumeric():
        print("Enter the valid number")
        Loan = input("Enter the amount of the loan($): ")

    InterestRate = float(input("Enter the interest rate(%): "))
    Interestfloat = InterestRate * 0.01
    NumberOfDays = int(input("Enter number of days until it is due(days): "))

    Interestpay = float(Loan) * Interestfloat

    def InterestCalculator(N_Days):
        e = N_Days-1
        Interestpay = float(Loan) * Interestfloat * ((1+Interestfloat)**e)
        print(f"{i} - $  {Interestpay:.2f}"  )
        return(Interestpay)

    i=1
    while i<=NumberOfDays:
        InterestCalculator(i)
        
        i = i+1

    print("Total Owing ")

LoanCalculator()
