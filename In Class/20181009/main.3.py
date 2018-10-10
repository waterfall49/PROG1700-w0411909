
def addNumber(a,b):
    return(a+b)

def multiNumber(c,d):
    return(c*d)

def squreNumber(x):
    return multiNumber(x,x)

def printOne():
    return("one")

def printNine():
    return("nine")

def printNineOneOne():
    print(printNine()+printOne()+printOne())

print(printNineOneOne())    


add = addNumber(199,57)
print(add)  
print(addNumber(199,57))

a = input("a= ")
b = input("b= ")
add = addNumber(a,b)
print(add)



