
def main():

    countries = ["canada","korea","spain","laos","mexico"]

    addcountry = input("What country should you add in the list? ")
    addcountry.lower()

    while addcountry in countries : 
        print("That country is the list already")
        addcountry = input("What country should you add in the list? ")
        addcountry.lower()
    else :
        answer = input("Do you want to add it in the list(yes or no)? ")
        answer.lower()
        if answer == "yes":
            countries.append(addcountry)
            for c in countries:
                print(c)
        else:
            for c in countries:
                print(c) 

    def UpperCase(a):
        return(a.upper())

    up_country = map(UpperCase,countries)
    print(list(up_country))

main()
