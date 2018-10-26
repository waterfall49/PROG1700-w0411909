
title_page = ["My Title Page Program ", "Fabulous!!", "by", "Hyejung Bae(Cathy)"]

def boarder(): 
    text = "*" * 80
    print(text)

def clr_scr():
    i=1
    while i<=9 : 
        clr = "*" + " "*78 + "*"
        print(clr)
        i=i+1

def center(w):
    length = int(39-(len(w)/2))
    centertext = "*" + " "*length + w + " "*length + "*"
    print(centertext)  

boarder()
clr_scr() 

for words in title_page : 
    center(words)

clr_scr()
boarder()
