import logging

#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.basicConfig(filename='info.log', encoding='utf-8', level=logging.INFO)
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.WARNING)
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.ERROR)
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.CRITICAL)

# DEBUG 	Informacje potrzebne programiście
# INFO 	Potwierdzenie, że wszystko jest w porządku
# WARNING 	Informacja o tym, że coś się dzieje i powinniśmy podjąć jakieś akcje
# ERROR 	Wystąpił błąd, określona funkcja jest niedostępna
# CRITICAL 	Błąd, którego nie da się rozwiązać


# 1. break

def break_in_python():
    for letter in "Python":
        if letter == "h":
            break
        # instrukcja breake powoduje natychmiastowe wyjście z pętli w momencie spełnienia warunku
        logging.info("Current Letter :" + letter)


break_in_python()

# napisz funkcję, która pokaże pierwszych 30 liczby podzielnych przez 6 z zakresu n pierwszych 200 liczb naturalnych


def liczby_podzielne():
    n = 200
    licznik_iteracji = 1
    for i in range(1, n+1):
        if i % 6 == 0:
            if licznik_iteracji > 30:
                break
        logging.info("po 30 elemencie wychodzimy break z pętli")
        print(i)


liczby_podzielne()


# 2. continue
def continue_in_python():
    for letter in 'Python':     # First Example
        if letter == 'h':
            continue
        # instrukcja continue powoduje natychmiastowe przejście na górę pętli, gdy spełniony jest warunek,
        # pozwala to na pominięcie elementu którego dotyczy warunek i kontynuowanie do końca iteracji
        logging.info("iterujemy po literach, gdy dojdziemy do litery h, "
                     "litera zostanie pominięta, wrócimy na górę pętli i iteracja bedzie kontynuowana do końca")
        print('Current Letter :', letter)


continue_in_python()


