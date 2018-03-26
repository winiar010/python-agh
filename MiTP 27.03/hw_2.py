
# Kreator postaci
import random

points = random.randint(40, 90)

attributes = {
    "siła": 0,
    "budowa": 0,
    "zręczność": 0,
    "roztropność": 0,
    "inteligencja": 0,
    "charyzma": 0
}

for key in attributes.keys():
    attributes[key] += 5
    points -= 5

while points:

    print("\nStatystyki:\n")
    for key in attributes.keys():
        print("%s: %d" % (key, attributes[key]))

    print("\nPozostałe punkty: %d" % points)

    tmp_attribute = input("Która cecha? ").lower()

    if tmp_attribute in attributes.keys():
        if attributes[tmp_attribute] < 20:
            attributes[tmp_attribute] += 1
        else:
            print("\nCecha '%s' osiągnęła limit!\n" % tmp_attribute)
            continue
    else:
        print("\nNie ma takiej cechy!\n")
        continue

    points -= 1

print("\nStatystyki:\n")
for key in attributes.keys():
    print("%s: %d" % (key, attributes[key]))