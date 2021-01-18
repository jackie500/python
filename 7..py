#7. Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól és ABC sorrendben kiírja őket a képernyőre!

szavak = [input("szó1: "), input("szó2: "), input("szó3: ")]
szavak.sort()
print(szavak)