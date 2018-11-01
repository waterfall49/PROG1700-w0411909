def main():

    userNumbers = []
    print(userNumbers)


    def isANumber(userinput):
        if userinput.isnumeric():
            userNumbers.append(int(userinput))
        else:
            userinput = input("ERROR! Please enter a valid number! ")
            isANumber(userinput)


    def firstNum():
        number = input("Please enter the first number: ")
        return number


    def secondNum():
        number = input("Please enter the second number: ")
        return number

    def getHighestCommonDivisor(x,y):

        factors1 = []
        factors2 = []
        commonFactors = []
        for d in range(1, x + 1):
            if (x % d == 0):
                factors1.append(d)

        for d in range(1, y + 1):
            if (y % d == 0):
                factors2.append(d)

        for i in factors2:
            if i == i in factors1:
                commonFactors.append(i)


        userNumbers.append(max(commonFactors))
        return max(commonFactors)


    isANumber(firstNum())
    isANumber(secondNum())
    getHighestCommonDivisor(userNumbers[0], userNumbers[1])


    print("The Highest Common Divisor of {0} and {1} is {2}".format(userNumbers[0], userNumbers[1], userNumbers[2]))
    yesNo = input("would you like to try again y/n?")

    if yesNo ==  "y":
        main()




main()