#Zadanie 1
# Napisz algorytm, który sprawdzi, czy liczba jest parzysta
# BONUS pobierz liczbę od użytkownika
#dzielenie modulo
liczba_str = input()
liczba = int(liczba_str)
if liczba % 2 == 0:
    print("parzysta")
else:
     print("nieparzysta")

# Zadanie 2
# Poproś użytkownika o login (lub wpisz ręcznie)
# Sprawdź, czy zgadza się z "adamnowak" i wypisz informację
# (Dla loginów nie ma znaczenia wielkość liter)
login = input("Podaj login")
login = login.lower().replace(" ","")


if login == "adamnowak":
    print("poprawny login")
else:
    print("niepoprawny login")

# Zadanie 3
# Poproś użytkownika "adam" o nowe hasło
# Sprawdź, czy jego login się w nim zawiera
# (wielkimi lub małymi literami) i wypisz informację
login = "adam"
password = input("Podaj hasło: ")
if login in password:
    print("Hasło zawiera Twoje imię. Podaj nowe hasło.")
else:
    print("podaj hasło")


# Zadanie 4
# Poproś użytkownika o nowe hasło i sprawdź czy jest bezpieczne, tzn.:
# Ma 8 znaków lub więcej
# Nie zawiera roku 2019, ani miesiąca (obecnego, słownie, czyli "wrzesien", niezależnie od wielkości liter)
# Zawiera przynajmniej jeden znak specjalny "#", "@" lub "#"

password = input("Podaj hasło: ")

if len(password) >= 8:
    if "2019" not in password:
        if "wrzesień" not in password.lower():
            if "#" in password or "@" in password:
                print("OK")
            else:
                print("Hasło musi zawierać # lub @" )
        else:
            print("Hasło nie może zawierać nazwy obecnego miesiąca")
    else:
        print("Hasło nie może zawierać roku 2019")
else:
    print("Hasło musi zawierać co najmniej 8 znaków")


# Zadanie 5
# Poproś użytkownika o fragment tekstu, a następnie o słowo
# Określ na której pozycji rozpoczyna się dane słowo w danym tekscie używając metody find()
# Wypisz odpowiedni komunikat - jedne w przypadku sukcesu, drugi w przypadku porażki (braku słowa w tekscie)
#
# Np.:
# Dla tekstu "Ala ma kota" i słowa "kot"
# "Słowo "kot" znajduje się na 7 pozycji."
#
# Dla tekstu "Ala ma kota" i słowa "pies"
# "Słowo "pies" nie znajduje się w tekscie."

fragment_tekstu = input("Wpisz fragment tekstu: ")
słowo = input("Wpisz słowo: ")
index = fragment_tekstu.lower().find(słowo)

if słowo in fragment_tekstu:
    print("Słowo " + str(słowo) + " znajduje się w tekście na " + str(index) + " pozycji.")
else:
    print("Slowo nie występuje we wpisanym fragmencie tekstu.")

# Zadanie 6
# Rozwiń powyższy program dodając do komunikatu wizualizację:
# Wszystkie elementy tekstu które nie są pierwszym wystąpieniem słowa zamień na "_"
#
# Np.:
# Dla tekstu "Ala ma kota" i słowa "kot"
# "Słowo "kot" znajduje się na 7 pozycji."
# "Ala ma kota jhgjhgjjhgj"
# "_______kot_____________"
#
# Dla tekstu "Ala ma kota" i słowa "pies"
# "Słowo "pies" nie znajduje się w tekscie."
# "___________

# Uwaga! Zależy nam na wizualizacji, a nie wartości - użyj mądrego tworzenia stringa i indeksowania,
# a nie podmiany wartości.

fragment_tekstu = input("Wpisz fragment tekstu: ")
fragment_tekstu_małymi = fragment_tekstu.lower()
słowo = input("Wpisz słowo: ")
słowo_małymi = słowo.lower()


index = fragment_tekstu_małymi.find(słowo_małymi)

if słowo_małymi in fragment_tekstu_małymi:
    print("Słowo " + str(słowo) + " znajduje się w tekście na " + str(index) + " pozycji.")

    index_2 = index + len(słowo_małymi)
    myślniki_przed = "_" * index
    index_3 = len(fragment_tekstu)
    myślniki_po = "_" *(index_3 - index_2)
    print(myślniki_przed + słowo + myślniki_po)

else:
    print("Slowo nie występuje we wpisanym fragmencie tekstu.")

# Zadanie 7
# Pobierz liczbę od użytkownika
# Sprawdź czy użytkownik faktycznie podał liczbę (metoda isdigit() typu string)
# Jeżeli tak to sprawdź podzielność przez kolejno 3, 5 i 7 (nie naraz)
# Wypisz rezultat dla każdego sprawdzenia
# Np. dla liczby 21
# "Liczba 21 jest podzielna przez 3!"
# "Liczba 21 jest podzielna przez 7!"
liczba = input("Podaj liczbę: ")
if liczba.isdigit():
    if int(liczba) % 3 == 0:
        print("Liczba jest podzielna przez trzy.")
    else:
        print("Liczba nie dzieli się przez trzy.")
    if int(liczba) % 5 == 0:
        print("Liczba jest podzielna przez pięc.")
    else:
        print("Liczba nie jest podzielna przez pięć.")
    if int(liczba) % 7 == 0:
        print("Liczba jest podzielna przez siedem.")
    else:
         print("Liczba nie jest podzielna przez siedem.")
else:
    print("Podana wartośc nie jest liczbą")



# Zadanie 8
# Pobierz wynik sprawdzianu od użytkownika
# Sprawdź czy jest to liczba i czy jest z zakresu 0 do 100
# Wypisz ocenę na podstawie progu procentowego
# 5 od 90, 4+ od 80, 4 od 70, 3+ od 60, 3 od 50, 2 dla mniej niż 50

wynik_sprawdzianu = input("Podaj wynik sprawdzianu: ")
if wynik_sprawdzianu.isdigit():
    if int(wynik_sprawdzianu) in range(0,100):
        if int(wynik_sprawdzianu) >= 100*0.9:
            print("Twoja ocena to 5.")
        if int(wynik_sprawdzianu) >= 100 * 0.8 and int(wynik_sprawdzianu) < 100 * 0.9:
            print("Twoja ocena to 4+.")
        if int(wynik_sprawdzianu) >= 100 * 0.7 and int(wynik_sprawdzianu) < 100 * 0.8:
            print("Twoja ocena to 4.")
        if int(wynik_sprawdzianu) >= 100 * 0.6 and int(wynik_sprawdzianu) < 100 * 0.7:
            print("Twoja ocena to 3+.")
        if int(wynik_sprawdzianu) >= 100 * 0.8 and int(wynik_sprawdzianu) < 100 * 0.6:
            print("Twoja ocena to 3.")
        if int(wynik_sprawdzianu) <= 100 * 0.5:
            print("Twoja ocena to 2.")
    else:
        print("Podana liczba nie jest liczbą z zakresu od 0 do 100.")
else:
    print("Podana wartośc nie jest liczbą.")



# Zadanie 9
# Sprawdź czy jest wygrana w kółko i krzyżyk
# Wejście to 9 znaków oznaczających stan planszy w kolejnych wierszach - "x", "o", lub puste "-"
# Wypisz czy jest wygrana i czyja
# Sprawdź kilka planszy

plansza_1 = "xoo-xo--x"
plansza_2 = "xooxoo--x"
plansza_3 = "xooxoooxx"
