
def landscapecalculator():

    # There is a base labour charge of $1000
    # If the surface (length * width) is over 5000 square feet, add $500
    # The cost is calculated per square foot
    # If the grass is “fescue” the cost is $0.05; for “bentgrass” it is $0.02; “campus” is $0.01
    # Each tree requested has a $100 charge

    # input
    housenumber = input("Enter House Number: ")
    length = float(input("Enter property depth (feet): "))
    width = float(input ("Enter property width (feet): "))
    typeofgrass = input("Enter type of grass (fescue, bentgrass, campus): ")
    numberoftree = float(input("Enter the number of trees: "))

    # process
    labourcharge = 1000
    ratepertree = 100   # Each tree requested has a $100 charge
    addionalfee = 500   # If the surface (length * width) is over 5000 square feet, add $500

    def multiple(a,b):
        return(a*b)

    def add(c,d,e):
        return(c+d+e)    

    if typeofgrass == "fescue":
        cost = 0.05
    elif typeofgrass == "bentgrass":
        cost = 0.02
    elif typeofgrass == "campus":
        cost = 0.01
    else:
        cost = 0
        print("Enter the correct type of grass again :(")

    grasscost = multiple(multiple(length,width),cost)

    if multiple(length,width) > 5000:
        grasscost = grasscost + addionalfee
    else:
        grasscost = grasscost

    treecost = multiple(numberoftree,ratepertree)
    totalcost = add(labourcharge,grasscost,treecost)

    # output    

    print(f"Total cost for house {housenumber} is : ${totalcost:.2f} ")


landscapecalculator()