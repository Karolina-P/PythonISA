# Zadanie
# Zmienna dane zawiera 24 odczyty temperatury z 24 godzin
# Każde 4 znaki to jeden odczyt w setnych stopni Celsjusza,
# tzn "2150" to 21.50°C
# Pomiary są dokonane o pełnych godzinach od 00:00 do 23:00
# Wypisz do konsoli raport w formacie:
# <godzina>:<tabulator><stopnie z dokładnością do drugiego miejsca po przecinku><znak stopni>C
# Dla odczytów niższych niż lub równych 20°C dodaj "<tabulator>!"
# Dla odczytów niższych niż lub równych 18,5°C dodaj dodatkowy wykrzyknik
# Nie kopiuj proszę znaku stopni. Spróbuj użyć znaku unicode \u00b0
# Docelowy rezultat znajduje się poniżej
dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"

for pozycja in range(0, 24):
    start = pozycja * 4
    koniec = start + 4

    godzina = '{:02d}:00'.format(pozycja)
    odczyt = dane[start:koniec]
    odczyt_float = int(odczyt) / 100
    temperatura = '{:04.2f}\u00b0C'.format(odczyt_float)

    if odczyt_float <= 18.50:
        znacznik = '\t!!'
    elif odczyt_float <= 20.00:
        znacznik = '\t!'
    else:
        znacznik = ''

    print(godzina + ':\t' + temperatura + znacznik)

