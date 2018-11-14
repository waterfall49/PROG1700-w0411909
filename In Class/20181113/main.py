
infile = open("input.txt")

line_list = []
for line in infile : 
    mywords = line.split(' ')
    line_list.extend(mywords)
print(line_list)