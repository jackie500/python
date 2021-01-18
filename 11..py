#11. Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok összege!

szam = int(input("szám: "))
osszeg = 0
for i in range(szam, 0, -1):
    osszeg = osszeg + i
print(osszeg)

