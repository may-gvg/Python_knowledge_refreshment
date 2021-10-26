# operator == służy do porównywania wartości dwóch zmiennych,
# operator is sprawdza czy dwa obiekty mają takie samo miejsce w pamięci


lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print(lista1 is lista2)
print(lista1 == lista2)
print(lista1 is lista3)

print(id(lista1))
print(id(lista2))
print(id(lista3))


class Maciek:
    def __init__(self, age):
        self.age = age


instancja1 = Maciek(40)
instancja2 = Maciek(40)
# kopiowanie wskaźnika
instancja3 = instancja1
print(instancja1 is instancja2)
print(instancja1 is instancja3)


def funkcja(maciek):
    maciek.age = 41


# przekazanie wsaźnika do funkcji
funkcja(instancja1)
print(instancja1.age)

print(id(instancja1))
print(id(instancja2))
print(id(instancja3))
