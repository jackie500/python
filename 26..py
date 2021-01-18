# 26
"""
Írj egy Python programot, amely a temp.txt szöveges fájl minden második szavát (szóközzel
elválasztott részsztringjét) a képernyőre írja!
"""


f = open("temp2.txt")
fS = f.read()
f.close()

fSList = []

fSList = fS.split(" ")

for i in range(1, len(fSList), 2):
    print(fSList[i])



