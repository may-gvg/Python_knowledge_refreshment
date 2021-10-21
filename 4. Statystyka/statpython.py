# W statystyce przez populację rozumiemy zbiór wszystkich elementów,
# których dotyczy dana analiza.
# Próba będzie z kolei zawsze podzbiorem tej populacji.


# Miary położenia rozkładu


# 1. Średnia arytmetyczna
# Średnią cechę danej populacji możemy obliczyć, sumując ze sobą wszystkie obserwacje,
# a następnie dzieląc tę sumę przez liczbę wszystkich obserwacji.

# Jest to najbardziej popularna miara, jednak jej wadą jest podatnośc na wartości skrajne.
# Dla przykładu, dla zbioru: 1,2,3,4,5,6,7,8,9,66

# Pandas:
# df.describe()
# df.mean()

# Pyspark
# df.mean()

# Query sql:
# df.avg

# Python an piechotę:


expectancy_at_birth_list = [76.84878, 81.40732, 77.57895, 74.16341, 68.84907,
                            73.88595, 75.26829, 76.26098, 80.57244, 65.46259,
                            67.5482, 55.02451, 76.2799, 82.29024, 69.80695,
                            81.40112, 82.19756, 74.22683, 80.12888, 45.55095]

no_of_elements = len(expectancy_at_birth_list)


average_age = sum(expectancy_at_birth_list) / no_of_elements

print(f'{average_age = }')

# 2. Mediana

# Jest wartością środkową zbioru, w celu jej policzenia należy zbiór uszeregować rosnąco.
# Jest mniej podatna na wartości skrajne od średniej arytmetycznej.
# W przypadku zbioru nie parzystego będzie to wartość śrdokowa, w przypadku zbioru parzystego,
# będzie to średnia dwóch wartości środkowych.

# Pandas:
# df.median()

# Pyspark
# df.median()

# Query sql:
# mediana nie jest naturalną funkcją sql i w zasadzie możliwe do wyobrażenia, nie mniej bardzo złożoną querą

# Python an piechotę

expectancy_at_birth_list.sort()

num = no_of_elements // 2
mediana = (expectancy_at_birth_list[num] + expectancy_at_birth_list[num - 1]) / 2

print(f'{mediana = }')

# Dominanta - moda
# Najczęściej występująca obserwacja w rozkładzie. W przypadku zbioru,
# gdzie kazdy element występuje taką samą ilość razy, np. 1,2,3,4,5,6,7,8 – będziemy mieć sytuację gdzie dominanata nie występuje.

# Pandas:
# df.mode()
# df.value_counts()

# Pyspark
# df.mode()

# Query sql:
# SELECT ,  COUNT(*) AS `num`
# FROM  GROUP BY
# ORDER BY num DESC;


# Python an piechotę

# domina = max(set(expectancy_at_birth_list), key=expectancy_at_birth_list.count)
# domina2 = expectancy_at_birth_list

# print(domina2)


# Miary rozproszenia rozkładu
# Dzięki miarom rozproszenia rozkładu jesteśmy w stanie wyrazić liczbowo, jak szeroko rozłożone
# są poszczególne obserwacje wokół średniej arytmetycznej.

# Liczone są dla próby bądź populacji:


# Wariancję obliczamy jako sumę kwadratów odchylenia poszczególnych obserwacji od średniej,
# podzieloną przez liczbę obserwacji (w przypadku populacji)
# lub wielkość próby pomniejszoną o jeden (w przypadku próby).


# Odchylenie standardowe
# W praktyce najczęściej analizie poddaje się odchylenie standardowe, czyli pierwiastek kwadratowy wariancji,
# z uwagi na fakt, że podaje wartość w tej samej jednostce mierzalnej gdy wariacja jest w
# jednostkach kwadratowych. Odchylenie standardowe liczymy jako pierwiastek wariancji.


# Pandas:
# df.describe()
# df.std()

# Pyspark
# df.std()

# Query sql:
# df.std()


# Python an piechotę:

suma = 0
for age in expectancy_at_birth_list:
    b = (age - average_age) ** 2
    suma += b
wariancja = suma / (len(expectancy_at_birth_list) - 1)

print(f'{wariancja = }')

odchylenie_standardowe = wariancja ** (1 / 2)
print(f'{odchylenie_standardowe = }')

fertility_rate_list = [
    1.3, 1.95, 2.466, 1.6, 2.952,
    1.801, 1.34, 1.34, 1.63, 2.326,
    2.436, 6.563, 1.283, 1.43, 1.988,
    1.61, 1.921, 2.4, 1.495, 4.705]

no_of_elements = len(fertility_rate_list)

sum_of_fertility_element = 0
for rate in fertility_rate_list:
    sum_of_fertility_element = sum_of_fertility_element + rate

average_fertility = sum_of_fertility_element / no_of_elements

print(f'{average_fertility = }')

sum = 0
for age in fertility_rate_list:
    c = (age - average_age) ** 2
    sum += c
wariancja_fertility = sum / (len(fertility_rate_list) - 1)

print(f'{wariancja_fertility = }')

odchylenie_standardowe_fertility = wariancja_fertility ** (1 / 2)

print(f'{odchylenie_standardowe_fertility = }')

# Kowiaracja i korelacja
# Miary kwantyfikujące relację pomiędzy dwiema zmiennymi.

# Co zatem możemy powiedzieć o tym współczynniku korelacji?

# Współczynnik korelacji na poziomie 0 oznacza, że obie zmienne są niezależne od siebie i nie ma pomiędzy
# nimi żadnej relacji.

# Współczynnik korelacji poniżej zera oznaczałby, że zachodzi korelacja ujemna, tj. wzrost wartości jednej
# zmiennej przekłada się na spadek wartości drugiej zmiennej.

# Współczynnik korelacji powyżej zera oznacza, że mamy do czynienia z korelacją dodatnią, więc wzrost wartości
# jednej zmiennej przekłada się na wzrost wartości drugiej zmiennej.


expectancy_at_birth_list2 = [76.84878, 81.40732, 77.57895, 74.16341, 68.84907,
                             73.88595, 75.26829, 76.26098, 80.57244, 65.46259,
                             67.5482, 55.02451, 76.2799, 82.29024, 69.80695,
                             81.40112, 82.19756, 74.22683, 80.12888, 45.55095]

sum = 0
l = len(fertility_rate_list)
for i in range(l):
    sum += (expectancy_at_birth_list2[i] - average_age) * (fertility_rate_list[i] - average_fertility)

kowariancja = sum / (l - 1)

print(f'{kowariancja = }')

wspolczynnik_korelacji = kowariancja / (odchylenie_standardowe - odchylenie_standardowe_fertility)
print(f'{wspolczynnik_korelacji = }')

###0,1<|r|≤0,3 – korelacja słaba
# Korelacja słaba - wskazuje na fakt, że dobrze się rozmnażać i poprawia to długość życia ale bez przesady
# i z umiarem ;)


# Na koniec postaraj się oszacować średnią oczekiwaną długość życia dla całej populacji przy poziomie ufności 95%.
# poziom istotności na poziomie 0,05
# Przyjmij, że odchylenie standardowe populacji wynosi 9,09.

x = poziom_istotnosci = 0.05
y = ochylenie_pop = 9.09
przedzial_ufnosci = average_age - x * (y / (no_of_elements ** (1 / 2))), \
                    average_age + x * (y / (no_of_elements ** (1 / 2)))

print(f'{przedzial_ufnosci = }')

# Wartość ze znormalizowanego rozkładu normalnego odpowiadająca przyjętemu poziomowi istotności
# EDIT
wartosc_znormalizowana = average_age - (average_age - x * (y / (no_of_elements ** (1 / 2))))

wartosc_znormalizowana1 = average_age - (average_age + x * (y / (no_of_elements ** (1 / 2))))

print(f'{wartosc_znormalizowana = }')
print(f'{wartosc_znormalizowana1 = }')
