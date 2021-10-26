# Literal String Interporation
# f - strings
import datetime

imie = "Maciek"

wiek = 26

zadanie = f"zad1: Hello nazywam się {imie} i mam {wiek} lat"

print(zadanie)

# wywoływanie metod na obiektach przekazanych do f stringa

imie = "Maciek"

wiek = 26

# = pokazuje zmienną i wartość
zadanie1 = f"zad1: Hello nazywam się {imie=} i mam {wiek=} lat"

print(zadanie1)

imie = "Maciek"

wiek = 26

zadanie2 = f"zad2: Hello nazywam się {imie.upper()} i mam {wiek} lat"

print(zadanie2)

# z wywołniem funkcji
imie = "Maciek"

wiek = 26


def print_text():
    return "!!!"


zadanie3 = f"zad3: {print_text()}Hello nazywam się {imie.upper()} i mam {wiek} lat"

print(zadanie3)

num = 7
zadanie4 = f"zad4: {num ** 2}"

print(zadanie4)

# formatowanie
num = 7.5
zadanie5 = f"zad5: {num:.2f}"

print(zadanie5)

# po ,
num = 1234567
zadanie6 = f"zad6: {num:,}"

print(zadanie6)

# binarnie
num = 144
zadanie7 = f"zad7: {num:b}"

print(zadanie7)

# num to asci
num = 65
zadanie8 = f"zad8: {num:c}"

print(zadanie8)

# fstring data

now = datetime.datetime.now()
print(now)
print(f"{now:%y-%m-%d}")
# lepsza konstrukcja
print(f"{now:%Y-%m-%d}")
print(f"{now:%Y-%m-%d %H-%M}")

# formatowanie odstępu, fstring w słowniku
name_and_age = {"maciek": 66,
                "joanna": 33,
                "miłosz": 37,
                "bardzo długie imię ": 57}

for name, age in name_and_age.items():
    print(f"{name} {age}")

for name, age in name_and_age.items():
    print(f"opcja 2: {name:30} {age}")
