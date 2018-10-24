
def LoanCalculator():

    import math

    Loan = input("Enter the amount of the loan($): ")

    while not Loan.isnumeric():
        print("Enter the valid number")
        Loan = input("Enter the amount of the loan($): ")

    InterestRate = float(input("Enter the interest rate(%): "))
    Interestfloat = InterestRate * 0.01  # Convert % to float to calculate
    NumberOfDays = int(input("Enter number of days until it is due(days): "))

    Interestpay = float(Loan) * Interestfloat  # Interestpay 

    def InterestCalculator(D_days):        # Function to calculate accumulate interestpay
        additionalpay = Interestpay * Interestfloat
        I_Interestpay = Interestpay + additionalpay
        print(f"{D_days} - $  {I_Interestpay:.2f}  |" +  "=" * math.ceil(I_Interestpay) )
        return(D_days,I_Interestpay)     

    i=1
    while i<=NumberOfDays:
        if i == 1: 
            print(f"\n{i} - $  {Interestpay:.2f}  |" +  "=" * math.ceil(Interestpay) )
            Totalpay = Interestpay + float(Loan)   # Totalpay is includng loan money
        else:
            Day,Interestpay=InterestCalculator(i)
            Totalpay = Totalpay + Interestpay  # Totalpay is accumulated 
        i = i+1

    print(f"\nTotal Owing : ${Totalpay:.2f} ")

LoanCalculator()
