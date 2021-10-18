import logging

logging.basicConfig(filename='DEBUG.log', encoding='utf-8', level=logging.DEBUG)


# DEBUG 	Informacje potrzebne programiście
# INFO 	Potwierdzenie, że wszystko jest w porządku
# WARNING 	Informacja o tym, że coś się dzieje i powinniśmy podjąć jakieś akcje
# ERROR 	Wystąpił błąd, określona funkcja jest niedostępna
# CRITICAL 	Błąd, którego nie da się rozwiązać


class Ptak:
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lec(self):
        logging.debug("Tu " + self.gatunek + ". Startuje, osiagam maksymalnie " + str(self.szybkosc))


class Orzel(Ptak):
    def __init__(self, szybkosc):
        super().__init__("Orzel", szybkosc)

    def polowanie(self):
        logging.debug("Tu " + self.gatunek + ". Rozpocząłem polowanie")

    def jaki_odglos(self):
        logging.debug("argh")


class Czapla(Ptak):
    def __init__(self, szybkosc):
        super().__init__("czapla", szybkosc)

    def polow(self):
        logging.debug("Tu " + self.gatunek + ". Tu łowię rybkę")

    def lec(self):
        logging.debug("Tu " + self.gatunek + ". Nie lecę, będę jadł " + str(self.szybkosc))

    def jaki_odglos(self):
        logging.debug("brbrbr")


# Orzeł
Ptak_o = Orzel(34)
Ptak_o.lec()
Ptak_o.polowanie()

# Czapla
Ptak_c = Czapla(21)
Ptak_c.lec()
Ptak_c.polow()
