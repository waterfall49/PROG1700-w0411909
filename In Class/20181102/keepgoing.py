
def printFactors(n):
    FL = []
    for i in range(1,n+1) : 
        if n % i == 0 :
            FL.append(i)
    print(FL) 

def main():
    KeepGoing = "y"
    while KeepGoing == "y" : 
        num = int(input("Enter the number: "))
        printFactors(num)
        KeepGoing = input("Do you want to keep going(y/n) ")
main()
