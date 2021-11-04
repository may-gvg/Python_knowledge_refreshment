# Mapowanie
# map jest jak czarne pudełko do którego przekazywane są: 1. funkcja, 2. kolekcja ,
# efektem jest wykonanie funkcji na każdym elemencie kolekcji
# mapa modyfikuje każdy argument przepuszczająć go przez funkcję

kolekcja = [1, 2, 3, 4, 5, 6, 7]


def kwadraty(x):
    return x ** 2


wymapowany = map(kwadraty, kolekcja)

print(wymapowany)
print(list(wymapowany))

wymapowany2 = map(lambda x: x ** 2, kolekcja)

print(list(wymapowany2))

# Filtrowanie
# w sumie zachodzi samoistnie za kazdym razem gdy używamy if, czy tworzymy jakiś warunek, filter przepuszcza
# przez warunek kolekcję i pozostawia elementy dla których warunek był true

list_comp_filtred = [x ** 2 for x in kolekcja if x < 4]
print(list_comp_filtred)

wyfiltrowana = filter(lambda x: x % 2 == 0, kolekcja)
print(list(wyfiltrowana))
