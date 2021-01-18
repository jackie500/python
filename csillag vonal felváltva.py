
ok = True
number = int(input("Adj meg egy szamot: "))

for i in range(number):
    if ok:
        print("-", end="")
        ok = False
    else:
        print("*", end="")
        ok = True