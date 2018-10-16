
def mobiledataplan():

    # input
    data = float(input("Enter data usage (Mb): "))

    # process
    def multiple(a,b):
        return(a*b)

    def add(c,d,e):
        return(c+d+e)

    def subtract(f,g):
        return(f-g)

    # Up to and including 200Mb : $20.00 flat rate
    low_flatrate = 20
    # Over 1Gb : $118.00 flat rate
    high_flatrate = 118
    # Over 200Mb and up to and including 500Mb : $0.105 per Mb 
    rateperMB1 = 0.105
    # Over 500Mb and up to and including 1Gb : $0.110 per Mb
    rateperMB2 = 0.110

    # datarange is divided 2 section
    data1=subtract(data,200) 
    data2=subtract(500,200)
    data3=subtract(data,500)  

    if data <= 200 :
        rate = low_flatrate
    elif data > 200 and data <= 500 :
        additionrate1 = multiple(data1,rateperMB1)
        rate = add(low_flatrate,additionrate1,0)
    elif data > 500 and data <= 1000 : 
        additionrate1 = multiple(data2,rateperMB1)
        additionrate2 = multiple(data3,rateperMB2)
        rate = add(low_flatrate,additionrate1,additionrate2)
    else: 
        rate = high_flatrate
        
    # output    

    print(f"Total charge is ${rate:.2f} ")


mobiledataplan()