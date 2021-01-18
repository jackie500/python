
szám1 = int(input("szám1: "))
szám2 = int(input("szám2: "))
szám3 = int(input("szám3: "))

összeg1 = szám1 + szám2
összeg2 = szám1 + szám3
összeg3 = szám2 + szám3


if összeg1 == szám3:
    print("igen a", szám1, "és", szám2, " összege  egyenlő", szám3, "-al")

elif összeg2 == szám2:
    print("igen a", szám1, "és", szám3, " összege  egyenlő", szám2, "-al")

elif összeg3 == szám1:
    print("igen a", szám2, "és", szám3, " összege  egyenlő", szám1, "-al")
else:
    print("semelyik számpáros összege nem egyenlő a harmadik számmal ")
