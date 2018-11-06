import random

o = random.randint(1,25)
la = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s', \
		  't','u','v','w','x','y','z']
p = [' ', '.',',']
fr = "test_file.txt"
am = "r"
fw = "processed.txt"
e = "utf-8"
om = ""

mf = open(fr,am)
im = mf.read()

for i in range(len(im)):
	if im[i] in p:
		om += im[i]
	else:
		ai = la.index(im[i].lower())
		
		ni = (ai + o) % 26
		
		if im[i].upper() == im[i]:
			om += la[ni].upper()
		else:
			om += la[ni]

print(om)

