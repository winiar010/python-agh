#system walki

import random
import sys

enemies = {
    "Ork": {
        "health": 200},
    "Goblin": {
        "health": 100}
}

hero_health = 300


def fight(hero_health_point, enemy):
    enemy_health_point = enemies[enemy]["health"]

    while hero_health_point > 0 and enemy_health_point > 0:
        # Kolej gracza
        attack = random.randint(0, 20)
        enemy_health_point -= attack
        sys.stdout.write("\033[0;32m")
        print("Gracz zadał %s %d obrażeń." % (enemy+"owi", attack))
        if enemy_health_point <= 0:
            sys.stdout.write("\033[0;0m")
            print("\nWygrał gracz! Pozostało mu %d punktów życia." % hero_health_point)
            break

        # Kolej przeciwnika
        attack = random.randint(0, 20)
        hero_health_point -= attack
        sys.stdout.write("\033[1;31m")
        print("%s zadał graczowi %d obrażeń." % (enemy, attack))
        if hero_health_point <= 0:
            sys.stdout.write("\033[0;0m")
            print("\nWygrał %s! Pozostało mu %d punktów życia." % (enemy, enemy_health_point))
            break


fight(hero_health, "Ork")