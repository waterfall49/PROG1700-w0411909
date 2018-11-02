
def getFactorList(n):
    FL = []
    for i in range(1,n+1) : 
        if n % i == 0 :
            FL.append(i)
    return(FL)    

def max(L):
    max = L[0]
    for i in L :
        if i > max :
            max = i
    return(max)

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    FL1 = getFactorList(num1)
    FL2 = getFactorList(num2)
    print(FL1)
    print(FL2)
    max(FL1)
    print(max)
     
main()    


