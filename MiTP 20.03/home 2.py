# Maksymalne obciążenie

import random

HERO_WEIGHT = 80
max_weight = HERO_WEIGHT / 10
item_weight = 0

inventory = tuple(input("Co chcesz dodać do swojego ekwipunku? (elementy dodajemy po przecinku) ").split(","))

for item in inventory:
    item_weight += random.randint(1, 5)

if item_weight > max_weight:
    print("Przekroczono limit obciążenia!")
else:
    for item in inventory:
        print(item)