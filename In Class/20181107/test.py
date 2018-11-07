inp_obj = open("test.txt")
out_obj = open("outfile.txt","w")
for line_str in inp_obj:
    out_obj.write(line_str)
a = out_obj.seek(1)
print(a)
# out_obj = open("outfile.txt")
#print(out_obj.read())

inp_obj.close()
out_obj.close()