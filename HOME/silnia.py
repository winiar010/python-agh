#silnia

def silnia(liczba):
    if ((liczba == 0) or (liczba == 1)): return 1
    return silnia(liczba-1)*liczba


liczba = int(input("Podaj liczbe: "))
print(silnia(liczba))