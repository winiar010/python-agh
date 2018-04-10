# Funkcja postaci
import random


class Hero:

    hero = {}

    @staticmethod
    def create_hero():
        name = input("Podaj imię swojej postaci: ")

        Hero.hero["name"] = name

        points = random.randint(40, 90)

        attributes = {
            "siła": 0,
            "budowa": 0,
            "zręczność": 0,
            "roztropność": 0,
            "inteligencja": 0,
            "charyzma": 0
        }

        Hero.hero["attributes"] = {}

        for key in attributes:
            Hero.hero["attributes"][key] = 0
            Hero.hero["attributes"][key] += 5
            points -= 5

        while points:

            print("\nStatystyki:\n")
            for key in attributes:
                print("%s: %d" % (key, Hero.hero["attributes"][key]))

            print("\nPozostałe punkty: %d" % points)

            tmp_attribute = input("Która cecha? ").lower()

            if tmp_attribute in attributes:
                if Hero.hero["attributes"][tmp_attribute] < 20:
                    Hero.hero["attributes"][tmp_attribute] += 1
                else:
                    print("\nCecha '%s' osiągnęła limit!\n" % tmp_attribute)
                    continue
            else:
                print("\nNie ma takiej cechy!\n")
                continue

            points -= 1


hero = Hero
hero.create_hero()

print("\n%s" % hero.hero["name"])

for key in hero.hero["attributes"]:
    print("%s: %d" % (key, hero.hero["attributes"][key]))