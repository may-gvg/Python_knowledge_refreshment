import logging

logging.basicConfig(filename='info.log', encoding='utf-8', level=logging.INFO)

# 1. znajdz literę

string = "Python"
letter = "o"


def znajdz_litere(letter):
    for i in string:
        if i == letter:
            logging.info("znaleziono")
            break
    else:
        logging.info("nie znaleziono")


znajdz_litere(letter)

print('')


# liczby podzielne


def liczby_podzielne(n, wystapienia, liczba):
    licznik_iteracji = 1
    lista = []
    for i in range(1, n):
        if licznik_iteracji > wystapienia:
            break
        elif i % liczba == 0:
            lista.append(i)
            licznik_iteracji += 1
    return lista


wynik = liczby_podzielne(200, 30, 6)
print(f'liczby podzielne to: {wynik}')

print('')


def liczby_podzielne2(n, liczba, wystapienia):
    lista = []
    for i in range(1, n + 1):
        if i % liczba == 0:
            lista.append(i)
    return lista[:wystapienia]


wynik1 = liczby_podzielne2(200, 6, 30)
print(f"Listy podzielne2 to: {wynik1}")
