import random

liczby = set()
while len (liczby) < 6:
    liczba = random.randint(8,25)
    print("Wylosowano: ", liczba)
    liczby.add(liczba)
print("Wylosowałeś: ", liczby)