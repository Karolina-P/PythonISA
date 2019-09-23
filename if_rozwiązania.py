# Zadanie 5
# Poproś użytkownika o fragment tekstu, a następnie o słowo
# Określ na której pozycji rozpoczyna się dane słowo w danym tekscie używając metody find()
# Wypisz odpowiedni komunikat - jedne w przypadku sukcesu, drugi w przypadku porażki (braku słowa w tekscie)
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
# "_" * len("jfhtytfy")
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