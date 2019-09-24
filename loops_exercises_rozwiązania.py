# Zadanie 1 - while
# Napisz mini-encyklopedię Trójmiasta
# Program powinien prosić użytkownika o podanie pojęcia dopóki nie wpisze on komendy "koniec"
# Wszystkie hasła i komendy powinny być obsługiwane niezależnie od wielkości liter.
# W odpowiedzi na znane hasła powinien wypisać odpowiednią informację (treść dowolna):
# Dla "Gdańsk" lub "gdansk":
#   "Miasto na prawach powiatu w północnej Polsce w województwie pomorskim, położone nad Morzem Bałtyckim
#    u ujścia Motławy do Wisły nad Zatoką Gdańską."
# Dla "Sopot":
#   "Najdłuższe drewniane molo w Europie i kluby."
# Dla "Gdynia":
#   "Contrast Cafe i Teatr Muzyczny!"
# Dla wszystkich innych haseł:
#   "Przepraszam, nie mam informacji na ten temat."


czy_wyjsc = False
while czy_wyjsc == False:
     haslo = input("Podaj haslo: ")
     haslo = haslo.lower()

     if haslo == 'gdansk':
         print("Miasto na prawach powiatu w północnej Polsce w województwie pomorskim, położone nad Morzem Bałtyckim u ujścia Motławy do Wisły nad Zatoką Gdańską.")
     elif haslo == 'sopot':
         print("Najdłuższe drewniane molo w Europie i kluby.")
     elif haslo == 'gdynia':
         print("Contrast Cafe i Teatr Muzyczny!")
     elif haslo == 'koniec':
         czy_wyjsc = True
     else:
         print("Przepraszam, nie mam informacji na ten temat.")


# Zadanie 2 - while
# Wypisz liczby należące do ciągu Fibonacciego mniejsze od 100


 x = 0
 y = 1
 while y < 100:
     print(y)
     x = y
     y = x + y


# Zadanie 3 - while
# Do programu echo v2 dopisz wersję premium
# W normalnym trybie program powinien powtarzać to co wpisze użytkownik.
# Po wpisaniu tajnego hasła "tajny-kod-premium-2019" program będzie wypisywał bardziej skomplikowane echo:
# całość tekstu, całośc tekstu małymi literami, połowa tekstu małymi literami, 1/4 tekstu małymi literami, "..."
# Wszystko rozdzielone spacją, długości fragmentów zaokrąglone w dół
#
# Np.: na hasło "Echo"
# "Echo echo ec e ..."
# na hasło "Ala ma kota"
# "Ala ma kota ala ma kota ala m al ..."
# na hasło "AA"
# "AA aa a <puste> ..."

# Zadanie 4 - for
# Dla liczb od 1 do 100 (włacznie)
# Jeśli podzielna tylko przez 3 to napisz Fizz
# Jeśli podzilena tylko przez 5 to napisz Buzz
# Jeśli podzielna przez 3 i przez 5 to napisz FizzBuzz


 for liczba in range(1, 101):
     if liczba % 3 and liczba % 5:
         print('FizzBuzz')
     if liczba % 3:
         print('Fizz')
     elif liczba % 5:
         print('Buzz')


# Zadanie 5 - for
# Napisz licznik litery "a" w tekscie
# Program powinien przyjąć od użytkownika dowolny tekst,
# a następnie wypisać liczbę wystąpień znaku "a" (tylko małej)
# Zadanie zrealizuj przy pomocy pętli for
#
# Np.: dla tekstu "Ala ma kota"
# Wynik to 3


 tekst = "Ala ma kota"
 ilosc_a = 0
 for znak in tekst:
     if znak == 'a':
        ilosc_a = ilosc_a + 1

 print("Wynik to: " + str(ilosc_a))


# Zadanie 6 - for
# Napisz program który zobrazuje indeksowanie stringów
# Program powinien przyjąć od użytkownika dowolny tekst,
# a następnie wypisać co linię kolejny znak w cudzysłowie, jego indeks dodatni i indeks ujemny
#
# Np.:
# Podaj tekst:
# rafal
# "r" 0 -5
# "a" 1 -4
# "f" 2 -3
# "a" 3 -2
# "l" 4 -1


 fraza = input("Podaj tekst: ")
 dlugosc_frazy = len(fraza)
 index = 0
 for znak in fraza:
     print(f'"{znak}" {index} -{dlugosc_frazy-index}' )
     index = index + 1


# Zadanie 7
# Przyjmij dowolny tekst od użytkownika
# Policz ile jest samogłosek, a ile spółgłosek i wypisz wynik



# Zadanie 8
# Pobierz liczbę od użytkownika (upewnij się, że faktycznie jest to liczba)
# Wymaluj pramidę tej wysokości z liter "M"
# Np.: dla liczby 4
#
#    M
#   MMM
#  MMMMM
# MMMMMMM


 pietra = input("Podaj liczbe")
 if pietra.isnumeric() == False:
     print('Nie podałeś liczby')
 pietra = int(pietra)

 for liczba in range(0, pietra):
     if (liczba == 0):
         print( (pietra-liczba) * " " + "M" )
     else:
         print( (pietra-liczba) * " " + ((2*liczba)+1) * "M" )


# Spróbuj rozwiązać zadanie na dwa sposoby - z użyciem i bez użycia metody center() typu string

# Zadanie 9 - najtrudniejsze i największe
# Napisz gre "kółko i krzyżyk"
# Wyświetlaj aktualny stan planszy przy pomocy znaków 'o', 'x', '-' w trzech wierszach
# Np.:
#
# --x
# -x-
# oo-
#
# Naprzemiennie pytaj gdzie postawić 'x', a gdzie 'o' przyjmując numer pozycji od 1 do 9
# Tzn.:
#
# 123
# 456
# 789
#
# Zakończ grę gdy jedna ze stron wygra, lub wszystkie miejsca będą zapełnione
# (BONUS - zakończ również, gdy nie ma możliwości wygranej, np. w takim ułożeniu:
#   xxo
#   oox
#   x--    )
#
# Na razie wyświetlaj wszystko po kolei, jedno pod drugim/
#
# Przykładowe wyjście
#
# Kołko i krzyżyk!
#
# ---
# ---
# ---
#
# Gdzie postawić 'x': 1
#
# x--
# ---
# ---
#
# Gdzie postawić 'o': 5
#
# x--
# -o-
# ---
#
# I tak dalej
