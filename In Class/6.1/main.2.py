
def LoanCalculator():

    import math

    Loan = input("Enter the amount of the loan($): ")

    while not Loan.isnumeric():
        print("Enter the valid number")
        Loan = input("Enter the amount of the loan($): ")

    InterestRate = float(input("Enter the interest rate(%): "))
    Interestfloat = InterestRate * 0.01
    NumberOfDays = int(input("Enter number of days until it is due(days): "))

    def InterestCalculator(N_Days):
        e = N_Days-1
        I_Interestpay = float(Loan) * Interestfloat * ((1+Interestfloat)**e)
        return(N_Days,I_Interestpay)

    i=1
    while i<=NumberOfDays:
        Day,Interestpay=InterestCalculator(i)
        print(f"{Day} - $  {Interestpay:.2f}  |" +  "=" * math.ceil(Interestpay) )
        i = i+1

    #print(f"Total Owing : ${Totalpay:.2f} ")

LoanCalculator()
