szam = int(input("szám: "))

if szam % 5 == 0 and szam % 3 == 0:
    print("igen, a ", szam, "osztható 5-el és 3-mal is.")
elif szam % 5 == 0 and szam % 3 > 0:
    print("igen, a ", szam, "osztható 5-el,de nem oszható 3-mal")
elif szam % 5 > 0 and szam % 3 == 0:
    print("igen, a ", szam, "osztható 3-al, de nem osztható 5-el.")
elif szam % 5 == 0 and szam % 3 == 0:
    print("a", szam, "nem osztható sem 3-mal, sem 5-el.")

print("\nvége")