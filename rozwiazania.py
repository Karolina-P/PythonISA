tekst = "Ala ma kota w butach"
tajna_wiadomosc = "piyStAhcoand ejmeys tt esżu p;e)r!!"

# Zadanie 1
# Ze zmiennej tekst pobierz piąty znak ("m") wykorzystując indeksowanie
print(tekst[4])

# Zadanie 2
# Ze zmiennej tekst pobierz pierwsze 3 znaki ("Ala") wykorzystując slicing
print(tekst[0:3])

# Zadanie 3
# Ze zmiennej tekst pobierz od 8 do 10 znaku ("kot") wykorzystując slicing
print(tekst[7:10])

# Zadanie 4
# Odczytaj tajną wiadomość pobierając co drugi znak ze zmiennej tajna_wiadomosc
# Wykorzystaj slicing (podaj krok)
print(tajna_wiadomosc[0:36:2])

# Zadanie 5
# To nie jedyna ukryta wiadomość!
# Odczytaj co drugi znak, ale od drugiego znaku
# Wykorzystaj slicing (podaj krok i start)
print(tajna_wiadomosc[1:36:2])

# Zadanie 6
# Wypisz do konsoli tekst "Twój wynik to: 5.0!"
# Wykorzystaj zmienną wynik i formatowanie stringa (f"", lub metoda .format())
wynik = 5.0
print("Twój wynik to {:.1f}!".format(wynik))

# Zadanie 7
# Wypisz tekst tak jak wyżej, ale zmień formatowanie na 3 miejsca po przecinku
# "Twój wynik to: 5.000!"
# Wykorzystaj formatowanie miejsc po przecinku (:.3f we właściwym miejscu)
print("Twój wynik to {:.3f}!".format(wynik))

# Zadanie 8
# Zmień wartość zmiennej wynik na 4.15
# Wypisz tekst z zadania 7 z nową wartością
wynik = 4.15
print("Twój wynik to {:.2f}!".format(wynik))
