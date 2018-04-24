#program różnica

def roznica():
    liczby = input("Podaj dwie liczby całkowite, które chcesz odjąć (oddziel przecinkiem): ")
    x, y = liczby.split(",")
    wynik = int(x) - int(y)
    print(wynik)

roznica()