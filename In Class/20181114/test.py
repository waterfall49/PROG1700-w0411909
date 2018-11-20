t1 = [ (1,2), (3,4), (5,6), (7,8), (9,10), (11,12) ]
t2 = [ (3,4), (11,12) ]
set(t2).issubset(t1)
# returns true

# or equivalent use '<=' so
set(t2) <= set(t1)
# returns true