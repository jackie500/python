# 21. Írj egy Python programot, amely bekér a felhasználótól egy mondatot (sztringet) és ennek szavait (szóközzel elválasztott részsztringjeit) fordított sorrendben kiírja a képernyőre!


mondat = "Írj egy Python programot"
x = mondat.split()

for i in range(len(x), 0, -1):
    i = i - 1

    print(x[i], end=" ")




#igy rövidebb:

""" 
mondat = "Írj egy Python programot"
x = mondat.split()[::-1]
print(x)

"""

