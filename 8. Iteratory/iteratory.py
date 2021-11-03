# itereator służy do przeglądania kolekcji: listy zbiory słowniki krotki sa iterowalne

lista = [1, 3, 4, 5]

iterator_listowy = iter(lista)
print(iterator_listowy)
# obiekt iteracyjny

print(next(iterator_listowy))
print(next(iterator_listowy))
print(next(iterator_listowy))
print(next(iterator_listowy))


# print(next(iterator_listowy))


# pokazał wyjątek Stop iteracji przeszliśmy cała kolekcję

# __iter__ inicjuje iteracje
# __next__ zwraca wartość elementu i przechodzi na nastepny
# informuje o zakończeniu  iteracji i zwraca wyjatek gdy dojdzie do końca
# funkcja for nie zwraca wyjątku kończy iteracje

class Sentence:
    def __init__(self, zdanie):
        self.zdanie = zdanie
        self.index = 0
        self.slowa = self.zdanie.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.slowa):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.slowa[index]


orginal = Sentence("To jest mój tekst")

for slowo in orginal:
    print(slowo)
