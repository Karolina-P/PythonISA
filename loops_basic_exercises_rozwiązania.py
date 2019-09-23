# Zadanie 1 - while
# Wyliczaj i wypisuj kolejne potęgi liczby 2 (od pierwszej)
# Przerwij, gdy wyliczona wartość jest większa niż 3000
# Zrób to na dwa sposoby: (a) bez break, (b) z break
wynik = 0
 x = 1
 while wynik < 3000:
     wynik = 2**x
     x = x + 1
     print(wynik)

wynik = 0
x = 1
while True:
    wynik = 2**x
    if wynik > 3000:
        break
    x = x + 1
    print(wynik)


# Zadanie 2 - while
# Pobieraj w kółko tekst od użytkownika
# Wypisz to co wpisał, ale wielkimi literami
# Przerwij, gdy wpisze "quit" lub "q"
# Zrób to na dwa sposoby: (a) bez break, (b) z break

czy_zamknac_program = False
while czy_zamknac_program == False:
    tekst = input("Wpisz tekst: ")
    print(tekst.upper())
    if tekst == "quit" or tekst == "q":
        czy_zamknac_program = True

while True:
    tekst = input("Wpisz tekst: ")
    print(tekst.upper())
    if tekst == "quit" or tekst == "q":
        break


# Zadanie 3 - for
# Przejdź przez zmienną tekst znak po znaku
# Za każdym razem gdy natrafisz na spację, wypisz "Spacja!"
tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

tekst = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
for znak in tekst:
    if znak == " ":
        print("spacja")


# Zadanie 4 - for
# Dla liczb z zakresu od 1 do 15 (włącznie)
# Wypisz ich wartość do drugiej potęgi

liczby = range(1, 16)
for liczba in liczby:
    print(liczba**2)
