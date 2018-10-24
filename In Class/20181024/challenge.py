
def main():

    # input
    L = ["apples", "peaches", "grapes", "oranges", "bananas"]
 
    # process

    def UpperCase(str):
        STR=str.replace('e','E')
        return(STR)

    up_fruit = map(UpperCase,L)
    print(list(up_fruit))

    for w in L :
        if ("e" in w):
            A = w.index("e")
            print(f"{w} : {A}th character was e" )
        else:
            print(f"{w} : There is no e")

main()
