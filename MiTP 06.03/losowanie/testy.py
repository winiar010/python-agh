import random
# Losowa liczba od 0 do 1
print (random.random())
# Losowa wartosc miedzy 45-55
print (random.randint(45, 55))
# Losowa wartosc
print (random.choice( ["Andrzej", "Adam", "Zygmunt"] ))

from random import randint

times = input("Podaj liczbę losowań: ")

for x in range(int(times)):
    print("Wylosowano: ", randint(1, 6))
