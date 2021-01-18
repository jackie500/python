lista1 = ["alma", "körte", "alma", "körte"]
lista2 = ["alma", "körte", "barack"]

if len(lista1) > len(lista2) :
    print(" a  lista1 nagyobb mivel elemeinek száma: ", len(lista1), "\nlista1 elemei:", lista1)
elif len(lista1) == len(lista2):
    print("lista1 és lista2 egyenlő hosszuságu elemmel rendelkezik")

else:
    print("lista2 a nagyobb elemszámmal rendelkező lista")