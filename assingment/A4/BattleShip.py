
def main():

    table = [ [ 0 for i in range(6) ] for j in range(6) ]
    print(table)
    for d1 in range(6):
        for d2 in range(6):
            table[d1][d2]= d1+d2+2
    print(table)

if __name__ == "__main__":
    main()    
    