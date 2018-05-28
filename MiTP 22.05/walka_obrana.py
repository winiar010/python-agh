#Program na dwie klasy oddziałujące ze sobą

import random

class Hero(object):
    """Klasa bohatera"""
    def __init__(self,hp=100):
        self.hp=hp

    def heal(self):
        self.hp+=random.randint(1,8)
        if self.hp>100:
            self.hp=100
        print("Lekko się uleczyłeś, bohaterze!")

    def walcz(self,enemy):
        self.damage = 5 + random.randint(1,20)
        enemy.obrona(self.damage)

    def obrona (self,damage):
        print("Ała!")
        self.hp=self.hp-damage
        print("Pozostałe hp:",self.hp)

class Enemy(Hero):
    """Klasa przeciwnika"""
    def heal(self):
        self.hp+=random.randint(1,8)
        if self.hp>50:
            self.hp=50
        print("Lekko się uleczyłeś!")



def walka(hero,enemy):
    while hero.hp>0 and enemy.hp>0:
        choice = int(input("Spotykasz przeciwnika! Co chcesz zrobić? 1. Ucieczka 2. Walka:  "))
        if choice == 2:
            pass
        elif choice == 1:
            break
        hero.heal()
        enemy.heal()
        hero.walcz(enemy)
        if enemy.hp<0:
            break
        enemy.walcz(hero)

    if hero.hp > 0:
        print("Zwyciężył bohater!")
        print("Pozostałe hp bohatera:",hero.hp)
    else:
        print("Znowu w życiu Ci nie wyszło")
        print("Pozostałe hp przeciwnika:",enemy.hp)

#main
hero=Hero()
enemy=Enemy(50)
walka(hero,enemy)