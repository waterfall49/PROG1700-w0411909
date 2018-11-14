choices = ["chicken","iceberg","romantic i"]
strtemplete = "The _1_ jump over the _2_ to get to their _3_"

strtemplete = strtemplete.replace("_1_", choices[0])
strtemplete = strtemplete.replace("_2_", choices[1])
strtemplete = strtemplete.replace("_3_", choices[2])

for i in range(0,3):
    strPH = "_"
    strPH += str(i+1)
    strPH = "_"
    strtemplete = strtemplete.replace(strPH, choices[i])

print(strtemplete)