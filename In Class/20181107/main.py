s = 'Hello World'
str(s)
print(str(s))
print(repr(s))

print(str(1/7))

for x in range(1,11) : 
    print(f'{x:5d} {x*x:5d} {x*x*x:5d}') 

for x in range(1,11) :
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1,11) :
    print(repr(x).ljust(2), repr(x*x).ljust(3), end=' ')
    print(repr(x*x*x).ljust(4))

for x in range(1,11) :
    print(repr(x).center(5), repr(x*x).center(5), end=' ')
    print(repr(x*x*x).center(5))