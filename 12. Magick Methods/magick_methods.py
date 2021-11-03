from faker import Faker

fake = Faker()


# Stwórz klasę, która będzie przechowywać informacje z jednej wizytówki.
# Przyjmij, że każda wizytówka zawiera dane takie jak: imię,
# nazwisko, nazwa firmy, stanowisko, adres e-mail, wiek.

class VisitCard:
    def __init__(self, imie, nazwisko, nazwa_firmy, adres, stanowisko, email, wiek):
        self.imie = imie
        self.adres = adres
        self.nazwisko = nazwisko
        self.nazwa_firmy = nazwa_firmy
        self.stanowisko = stanowisko
        self.email = email
        self.wiek = wiek
        self.slownik = {"a": 1, "b": 2}

    def __call__(self, wojtek):
        print(wojtek)

    def __getitem__(self, item):
        if item == 'name':
            return f'{self.imie} {self.nazwisko}'

    def __setitem__(self, index, value):
        if index == 'name':
            self.imie = value

    # Magick Methods

    # 1. __init__ metoda inicjalizacji klasy
    # 2. __iter__ __next__ magiczne matody iteracji,
    # 3. __str__ __repl__ metody reprezentacji obiektu
    # 4. __add__ __len__ metody matematyczne
    # 5. __set item, get item__ ustawia, pobiera item słownika

    #   Zmodyfikuj kod z poprzedniego ćwiczenia na temat książki adresowej tak,
    #   aby obiekt wizytówki przedstawiony jako string zawierał imię, nazwisko i adres e-mail osoby,
    #   do której należy wizytówka.

    def __str__(self):
        return f"{self.imie} {self.nazwisko}{self.email}"

    #
    # # Rozwiń program przechowujący wizytówki. Do klasy opisującej wizytówkę dodaj metodę contact(),
    #    # która wypisze na konsoli napis “Kontaktuję się z …”,
    #     # a na końcu wyświetli imię, nazwisko, stanowisko i adres e-mail osoby, z którą chcemy się skontaktować.
    #
    def contact(self):
        print(f"Kontaktuje się z {self.imie} {self.nazwisko} {self.stanowisko} {self.email}")

    def __add__(self, klient):
        result = self.wiek + klient.wiek
        return result

    def __len__(self):
        result = len(self.imie + self.nazwisko)
        return result

    def __reversed__(self):
        return reversed(self.imie)

    # W klasie przechowującej wizytówkę zdefiniuj dynamiczny atrybut (używając @property),
    # który będzie zwracał sumę długości
    # oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia
    # i nazwiska danej osoby.

    @property
    def name_size(self):
        return len(self.imie + " " + self.nazwisko)


#
#
# # Zdefiniuj listę, która będzie zawierała 5 wizytówek ludzi o losowych danych (dane możesz skopiować
# ze strony takiej jak Fake Name Generator.
#
klient_1 = VisitCard(imie="Marysia", nazwisko="Low", nazwa_firmy="Yellow", stanowisko="stomatolog",
                     adres="Wrocek, 18 procek ", email="marysia@gmail.com", wiek=18)
klient_2 = VisitCard(imie="Władek", nazwisko="High", nazwa_firmy="Red", stanowisko="kosmita",
                     adres="Cieszyn, 15 wzgórze ", email="wlasekgu@gmail.com", wiek=23)
klient_3 = VisitCard(imie="Olek", nazwisko="nice", nazwa_firmy="Grey", stanowisko="astronauta",
                     adres="Dubrownik, Havrsko Sunsko", email="olek@gmail.com", wiek=34)
klient_4 = VisitCard(imie="Marian", nazwisko="LOL", nazwa_firmy="Blue", stanowisko="lekarz",
                     adres="Fiesta Majorca, 6543 Island", email="marian@gmail.com", wiek=17)
klient_5 = VisitCard(imie="Piotrek", nazwisko="wow", nazwa_firmy="Black", stanowisko="gamer",
                     adres="Cubana 15, LA California", email="piotr@gmail.com", wiek=15)
klient_6 = VisitCard(imie=fake.name(), nazwisko="", nazwa_firmy=fake.company(), stanowisko=fake.job(),
                     adres=fake.address(), email=fake.email(), wiek=44)

# dir pokazuje lista funkcji i zmiennych jaką zawiera obiekt

print(dir(klient_1))

klient_1("wojtek")

wynik = klient_1 + klient_2
print(f" add {wynik}")
print(len(klient_1))
print(len(klient_2))
print(list(reversed(klient_1)))
print(klient_1['name'])  # getitem
klient_1['name'] = 'Sebastian'  # setitem
print(klient_1.imie)
print(klient_1)

print(klient_1.imie)
print(klient_1)

# Napisz funkcję, która tworzy instancje Twojej klasy reprezentującej wizytówkę. Używając biblioteki faker,
# którą opisaliśmy
# powyżej. Zapewnij losowość danych w każdej wizytówce, którą zwróci Twoja funkcja.

lista = [klient_1, klient_2, klient_3, klient_4, klient_5, klient_6]

#  Stwórz listę wizytówek, a następnie używając funkcji sorted(), ułóż ją na trzy sposoby – według imienia, nazwiska
#  oraz adresu e-mail.


lista2 = sorted(lista, key=lambda klient1: klient1.imie)
lista3 = sorted(lista, key=lambda klient1: klient1.nazwisko)
lista4 = sorted(lista, key=lambda klient1: klient1.email)

for i in lista:
    print(i.imie, i.nazwisko, i.nazwa_firmy, i.stanowisko)
print("Imie: " + i.imie)
print("Nazwisko: " + i.nazwisko)
print("Nazwa Firmy: " + i.nazwa_firmy)
print("Stanowisko: " + i.stanowisko)
print("Adres: " + i.adres)
print("e_mail: " + i.email)
print(f"wiek: {i.wiek}")

print("---")

for i in lista2:
    print("Imie: " + i.imie)
print("Nazwisko: " + i.nazwisko)
print("Nazwa Firmy: " + i.nazwa_firmy)
print("Stanowisko: " + i.stanowisko)
print("Adres: " + i.adres)
print("e_mail: " + i.email)
print(f"wiek: {i.wiek}")
print("---")

for i in lista3:
    print("Imie: " + i.imie)
print("Nazwisko: " + i.nazwisko)
print("Nazwa Firmy: " + i.nazwa_firmy)
print("Stanowisko: " + i.stanowisko)
print("Adres: " + i.adres)
print("e_mail: " + i.email)
print(f"wiek: {i.wiek}")
print("---")

for i in lista4:
    print("Imie: " + i.imie)
print("Nazwisko: " + i.nazwisko)
print("Nazwa Firmy: " + i.nazwa_firmy)
print("Stanowisko: " + i.stanowisko)
print("Adres: " + i.adres)
print("e_mail: " + i.email)
print(f"wiek: {i.wiek}")
print("---")


# Dysponujesz już całkiem rozbudowanym programem do obsługi wizytówek. Po dodaniu kilku elementów wyślij go Mentorowi.
#   Używając dziedziczenia, rozdziel podstawową klasę wizytówki na dwie osobne: pierwsza (BaseContact) powinna
#   przechowywać podstawowe dane
#   kontaktowe takie jak imię, nazwisko, telefon, adres e-mail. Za pomocą kolejnej klasy (BusinessContact) rozszerz
#   klasę bazową o przechowywanie
#   informacji związanych z pracą danej osoby – stanowisko, nazwa firmy, telefon służbowy.
#  Oba typy wizytówek, powinny oferować metodę contact(), która wyświetli na konsoli komunikat w postaci “Wybieram
#  numer +48 123456789 i
#  dzwonię do Jan Kowalski”. Wizytówka firmowa powinna wybierać służbowy numer telefonu, a wizytówka bazowa prywatny.
# Oba typy wizytówek powinny mieć dynamiczny atrybut label_length, który zwraca długość imienia i nazwiska danej osoby.
# Stwórz funkcję create_contacts, która będzie potrafiła komponować losowe wizytówki. Niech ta funkcja przyjmuje
# dwa parametry: rodzaj wizytówki oraz ilość. Wykorzystaj bibliotekę faker do generowania danych.


class BaseContact:
    def __init__(self, imie, nazwisko, email, telefon, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.telefon = telefon
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.email} {self.wiek}"

    def contact(self):
        print(f"Wybieram numer {self.telefon} {self.imie} {self.nazwisko}")

    @property
    def label_length(self):
        return len(f"{self.imie} {self.nazwisko}")


x = BaseContact(imie="Majkel", nazwisko="mekson", email="at@o6.pl", telefon="1234", wiek=37)
print(x)


# super w przypadku dziedziczenie weźmie zmienną property z klasy jedna wżej od tej z której się dziedziczy
class BusinessContact(BaseContact):
    def __init__(self, stanowisko, nazwa_firmy, telefon2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stanowisko = stanowisko
        self.nazwa_firmy = nazwa_firmy
        self.telefon2 = telefon2

    def contact(self):
        print(f"Wybieram numer {self.telefon2} i dzwonię do {self.imie} {self.nazwisko}")


x = BusinessContact(imie="Majkel", nazwisko="Maejkson", email="pulajla@v.pl", telefon="1234567890", stanowisko="ninja",
                    nazwa_firmy="gate", telefon2="9876543210", wiek=23)
print(x.contact())


# Napisz funkcję, która tworzy instancje Twojej klasy reprezentującej wizytówkę.
# Zapewnij losowość danych w każdej wizytówce, którą zwróci Twoja funkcja.


def generuj_wizytowki(rodzaj=BaseContact, ilosc=1):
    wizytowki = []
    if rodzaj == BaseContact:
        for i in range(0, ilosc):
            kontakt = BaseContact(imie=fake.name(), nazwisko="", telefon=fake.phone_number(), email=fake.email(),
                                  wiek=fake.random_number(digits=None) % 125)
            wizytowki.append(kontakt)
    if rodzaj == BusinessContact:
        for i in range(0, ilosc):
            kontakt = BusinessContact(imie=fake.name(), nazwisko="", telefon=fake.phone_number(), email=fake.email(),
                                      stanowisko=fake.job(), nazwa_firmy=fake.company(), telefon2=fake.phone_number(),
                                      wiek=fake.random_number(digits=None) % 125)
            wizytowki.append(kontakt)
    return wizytowki


wizytowki = generuj_wizytowki(BusinessContact, 10)
for i in wizytowki:
    print(i)
