from random import randint

"""
for i in range(3):
    kezdés = input("kezdés: ")
    if kezdés == "r":
        szam = randint(1, 6)
        print("a számod", szam)
    elif kezdés == "q":
        break
"""

kezdés = input("kezdéshez nyomj start -ot, kilépéshez quit-ot: ")
if kezdés == "quit":
    exit("kilépve")

while kezdés == "r" or "start":
    kezdés = input("\ndobás(r) \nkilépés(q): ")
    if kezdés == "q":
        exit("kilépve")
    szam = randint(1, 6)
    print("\na számod", szam)











