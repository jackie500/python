# 22. Írj egy Python programot, amely bekér a felhasználótól egy sztringet és ezt úgy íratja ki, hogy a szóköz karaktereket kihagyja!


mondat = input("ird be a mondatot: ")
x = mondat.replace(" ", "")
print(x)
