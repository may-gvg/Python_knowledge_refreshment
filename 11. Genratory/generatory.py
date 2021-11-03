# Op1

def kwadraty(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


my_nums = kwadraty([1, 2, 3, 4, 5, 6])

print(my_nums)

comp = [i * i for i in range(1, 9)]
print(comp)
# zmiana nawisu na okragły zmienia listę składaną w generator
gen = (i * i for i in range(1, 9))
print(gen)

# konwercja do listy
print(list(gen))


# tworząć generator pomijamy całą część appenda do listy,
# zostawiamy iterację i w miejscu return używamy yielda po którym zostaje zdefiniowany warunek
# generator jest iteratorem
# budowanie funkcji z generatorem, oszczędza czas i jest znacznie lżejsze dla pamięci,
# yield zapisuje wyniki iteracji z warunkiem, zamiast całego obiektu - czy jakoś tak

def kwadraty2(nums):
    for i in nums:
        yield i * i


my_nums = kwadraty2([1, 2, 3, 4, 5, 6])

print(my_nums)

# konwersja do listy
print(list(my_nums))
#
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

for nums in my_nums:
    print(nums)


# print(next(my_nums))

# Stop itereation

# op2
def liczby_podzielne2(n, liczba, wystapienia):
    lista = []
    for i in range(1, n + 1):
        if i % liczba == 0:
            lista.append(i)
    return lista[:wystapienia]


wynik1 = liczby_podzielne2(200, 6, 30)
print(f"Listy podzielne2 to: {wynik1}")


# generator


def liczby_podzielne3(n, liczba):
    for i in range(1, n + 1):
        if i % liczba == 0:
            yield i


wynik1 = liczby_podzielne3(200, 6)
print(f"Listy podzielne3 to: {wynik1}")

print(next(wynik1))
print(next(wynik1))
print(next(wynik1))
print(next(wynik1))
print(next(wynik1))

print("check")

for i in wynik1:
    print(i)
