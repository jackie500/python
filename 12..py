# 12. Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a képernyőre a szó betűit, úgy, hogy minden betű egy új sorba kerüljön!

szó = input("adjon meg egy szót: ")

for i in range(len(szó)):
    print(szó[i], end=" ")




