#liczby podzielne przez 3 i 5

def warunek():
    liczba = input("Wprowadź liczbę: ")
    liczba = int(liczba)
    if liczba <= 0:
        print("Podaj liczbę większą od 0")
    elif liczba % 3 == 0 or liczba % 5 == 0:
        print("Prawda")
        return 1
    else:
        print("Liczba nie jest podzielna ani przez 3 ani przez 5")

again = 'y'
while again == "y":
    warunek()

    again = input("Liczymy jeszcze raz? (y/n) ")
