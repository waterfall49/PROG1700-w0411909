
str = "supercalifraglistic"
for ltr in str:
    print(ltr)

words = ["apple","banana"]
for w in words:
    print(w)

str = "programming"
ph = 0
for l in str:
    if l == "g" and ph == 0:
        l = l.upper()
        ph = 1
    print(l) 
"""i=0
for l in str:
    if i == 3:
        l = l.upper()
    i += 1 # i = i + 1
    print(l)"""
