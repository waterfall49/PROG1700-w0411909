
def mobiledataplan():

    # input
    data = float(input("Enter data usage (Mb): "))

    # process
    def datarate(a,b):
        return(a*b)

    # Up to and including 200Mb : $20.00 flat rate
    low_flatrate = 20
    # Over 1Gb : $118.00 flat rate
    high_flatrate = 118
    # Over 200Mb and up to and including 500Mb : $0.105 per Mb 
    rateperMB1 = 0.105
    # Over 500Mb and up to and including 1Gb : $0.110 per Mb
    rateperMB2 = 0.110

    if data <= 200 :
        rate = low_flatrate
    elif data > 200 and data <= 500 :
        rate = datarate(data,rateperMB1)
    elif data > 500 and data <= 1000 : 
        rate = datarate(data,rateperMB2)
    else: 
        rate = high_flatrate
        
    # output    

    print(f"Total charge is ${rate:.2f} ")


mobiledataplan()