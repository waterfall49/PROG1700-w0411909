
choices = []
openfile = open("template.txt")
strtemplete = openfile.read()

for i in range(0,3):
    answer = input(f"Enter the choice{i+1} : ")
    choices.append(answer)

strtemplete = strtemplete.replace("_1_", choices[0])
strtemplete = strtemplete.replace("_2_", choices[1])
strtemplete = strtemplete.replace("_3_", choices[2])

print(strtemplete)