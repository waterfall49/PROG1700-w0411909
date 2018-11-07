inp_obj = open("test.txt")
out_obj = open("outfile.txt","w")

print(inp_obj.read())
#print(inp_obj.tell())
# inp_obj.seek(2)
print(inp_obj.read(2))



# strContent = inp_obj.readline()
# print(strContent)

for line_str in inp_obj:
    out_obj.write(line_str)
#print(out_obj.read())
#a = inp_obj.seek(1)
#print(a)

# out_obj = open("outfile.txt")
#print(out_obj.read())

inp_obj.close()
out_obj.close()