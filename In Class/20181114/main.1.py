
choices = []
openfile = open("template.txt")
strtemplete = openfile.read()

for i in range(0,3):
    answer = input(f"Enter the choice{i+1} : ")
    choices.append(answer)

for i in range(0,3):
    strPH = "_"
    strPH += str(i+1)
    strPH += "_"
    strtemplete = strtemplete.replace(strPH, choices[i])

print(strtemplete)
openfile.close()