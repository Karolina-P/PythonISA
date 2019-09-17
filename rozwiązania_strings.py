#Zadanie 1
# Przypisz zmiennej tekst następującą wartość: "lorem ipsum"
# Dodaj do niej dalszy ciąg: "dolor sit amet"
# Tak aby otrzymać "lorem ipsum dolor sit amet"
# Wypisz wartość w konsoli
tekst = "lorem ipsum"
print(tekst + " " + "dolor sit amet")
tekst = (tekst + " " + "dolor sit amet")

# Zadanie 2
# Wykorzystując indeksowanie na zmiennej tekst
# Utwórz zmienną fragment_1, która będzie zawierała "ipsum"
# Wypisz wartość w konsoli
fragment_1 = (tekst[6:11])
print(fragment_1)

# Zadanie 3
# Wykorzystując indeksowanie na zmiennej tekst i łączenie stringów
# Utwórz zmienną fragment_2, która będzie zawierała "lorem amet"
# Wypisz wartość w konsoli
fragment_2 =(tekst[:5] + " " + tekst[-4:])
print(fragment_2)


# Zadanie 4
# Wykorzystując indeksowanie na zmiennych tekst i fragment_1
# utwórz zmienną bledny_tekst, która będzie zawierała
# "lorem muspi dolor sit amet"
# Wypisz wartość w konsoli
bledny_tekst = (tekst[:5] + " " + fragment_1[::-1] + " " + tekst[12:])
print("======")

print(tekst)
print(fragment_1)
print(bledny_tekst)
print("======")

# Zadanie 5
#Wykorzystując escape character '\' wypisz jedną komendą tekst: "You're dead, evil AI!" - said John, "format C:\!"
print("zadanie5")
print("\"You're dead, evil AI!\" - said John,\"format C:\\!\"")

# Zadanie 6
# 41737 na 88615 programistów używa pythona
# Wypisz te wartość procentowo, z dokładnością do 1 miejsca po przecinku
# Wykorzystaj formatowanie wartosci liczbowych
print("Zadanie 6")
value = 41737/88615
print(f"{value:.1%}")

# Zadanie 7
# imie i nazwisko mamy małymi literami
# Zapisz do jednej zmiennej "user", oba z wielkiej
# np. Rafał Styrylski
# Wypisz do konsoli
print("Zadanie 7")
name = "karolina"
surname = "pociejewska"
user = (name.capitalize() + " " + surname.capitalize())
print(user)

# Zadanie 8
# Napisz program który sprawdzi i wypisze wartość boolean, czy podany plik jest obrazkiem
# Załóżmy, że obsługujemy następujące formaty: .bmp .png .jpg .jpeg
# Spróbuj zrealizować zadanie na dwa sposoby:
# a. Indeksowaniem
# b. wykorzystując metodę endswith()  # Metodzie endswith można przekazać krotkę (tuple), np.: ("aaa", "bbb")

print("Zadanie 8")
name_1 = "plik.bmp"
name_2 = "plik.png"
name_3 = "plik.jpg"
name_4 = "plik.jpeg"

this_is_image = (name_1[-4:] == ".bmp" or
            name_2[-4:] == ".png" or
            name_3[-4:] == ".jpg" or
            name_4[-5:] == ".jpeg")
print(this_is_image)
extensions = ("bmp",".png", ".jpg", ".jpeg")
print(name_1.endswith(extensions))



# Zadanie 9
# Napisz program który policzy ile razy Rihanna śpiewa "work" we fragmencie swojego utworu
# Wykorzystaj metodę count()
fragment_piosenki = """Work, work, work, work, work, work
You see me I be work, work, work, work, work, work
You see me do me dirt, dirt, dirt, dirt, dirt, dirt
There's something 'bout that work, work, work, work, work, work
When you a gon' learn, learn, learn, learn, learn, learn
Me na care if me tired, tired, tired, tired, tired, tired"""

print("Zadanie 9")
work_count = fragment_piosenki.lower().count("work")
print(work_count)

# Zadanie 10
# Napisz program, który sprawdzi ile znaków potrzeba, żeby Rihanna zmęczyła się własną piosenką,
# tzn., na ktorej pozycji znajduje się pierwsze wystąpienie słowa "tired" we fragmencie utworu
# Wykorzystaj metodę find()

print("Zadanie 10")
index = fragment_piosenki.lower().find("tired")
print(index)

# Zadanie 11
# Nie wszyscy muszą utożsamiać się z fragmentem piosenki - dostosujmy więc tekst do siebie
# Napisz program, który odpowiednio zamieni wszystkie wystąpienia słowów:
# "work" na "programming" (Uwzględnij pierwsze wystąpienie z wielkiej litery!),
# "dirt" na "python"
# Wykorzystaj metodę replace()
piosenka_programisty = \
    fragment_piosenki.replace("Work", "Programming").replace("work", "programming").replace("dirt", "python")
print(piosenka_programisty)