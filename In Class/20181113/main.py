
infile = open("input.txt")

line_list = []
word_list = []
for line in infile :
    line = line.replace("\n","") 
    line_list.append(line)
    word_list.extend(line)
    print(word_list)
for word in line_list : 
    print(word)
    word_list.append(word)
print(word_list)