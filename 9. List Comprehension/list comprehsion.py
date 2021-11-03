# Listy składane (ang. list comprehension) są potężnym narzędzie, które tworzy nową tablicę
# na podstawie innej tablicy.
# I to wszystko w jednej, czytelnej instrukcji.

# Przykładowo powiedzmy, że potrzebujemy stworzyć nową tablicę liczb całkowitych,
# które określają długość każdego słowa
# w pewnym napisie, ale pod warunkiem, że nie jest to słowo "nad".


napis = 'Odwazny rudy lis przeskoczyl nad spiacym wilczurem'
slowa = napis.split()  # tworzymy tablice ze slowami zawartymi w napisie
dlugosc_slow = []
for slowo in slowa:
    if slowo != 'nad':
        dlugosc_slow.append(len(slowo))

print(dlugosc_slow)

# Lista składana
# Jej podstawowa konstrukcja to:
# lowa lista =  [wyrażenie for element in lista]
# nowa lista = wyrażenie for iteracja + if warunek gdy chemy filtrować


dlugosc_slow2 = [len(slowo) for slowo in slowa if slowo != 'nad']

print(dlugosc_slow2)

# kwadraty

numbers = [1, 3, 5, 11, 20]
squares = []
for number in numbers:
    squares.append(number * number)
print(f"Na wstępie mieliśmy taką listę {numbers}")
print(f"A oto jej kwadraty {squares}")

# Dla powyższego zadania obliczenia kwadratów będzie to zapis jak poniżej:

squares = [number * number for number in numbers]
print(f"Te kwadraty {squares} uzyskano dzięki list comprehension")

# Ćwiczenie
# Poeksperymentuj z różnymi wyrażeniami wstawianymi zamiast number * number.

# [wyrażenie for element in lista if warunek]

numbers = [1, 2, 0, 3, 0, 0, 0]
squares = []
for number in numbers:
    if number > 0:
        squares.append(number * number)

# listy składana

numbers = [1, 2, 0, 3, 0, 0, 0]
squares = [number * number for number in numbers if number > 0]

# Ćwiczenie
# Zakoduj listę składaną, która tworzy nową listę z liczbami długość słów
# (obliczysz je funkcją len). Oto lista do przerobienia: ['Arystoteles','Platon','Sokrates'].

filozofowie = ['Arystoteles', 'Platon', 'Sokrates']
list2 = []
for nazwa in filozofowie:
    nazwa = len(nazwa)
    list2.append(nazwa)

print(list2)

lost5 = [len(nazwa) for nazwa in filozofowie]
print(f"{lost5}")

# usuń duplikaty
lst = [5, 1, 3, 2, 21, 21, 4, 4, 4, 4, 7, 11, 11, 11, 1, 1]
temp_list = []
[temp_list.append(i) for i in lst if i not in temp_list]
print(temp_list)

# better than ugly
set = set(lst)
lst2 = list(set)

print(lst2)
