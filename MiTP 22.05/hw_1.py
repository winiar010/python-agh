import random


class Hero(object):
    """Hero class"""

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.CONST_ATTACK = 5
        self.is_win = False

    def attack(self, enemy):
        """Attack method"""
        tmp_attack = random.randint(1, 20) + self.CONST_ATTACK
        enemy.defense(tmp_attack)
        print("%s zadał %d obrażeń %s" % (self.name, tmp_attack, enemy.race))

    def defense(self, attack):
        """Defense method"""
        self.hp -= attack


class Enemy(object):
    """Enemy class"""

    def __init__(self, race, hp):
        self.race = race
        self.hp = hp
        self.CONST_ATTACK = 5
        self.is_win = False

    def attack(self, enemy):
        """Attack method"""
        tmp_attack = random.randint(1, 20) + self.CONST_ATTACK
        enemy.defense(tmp_attack)
        print("%s zadał %d obrażeń %s" % (self.race, tmp_attack, enemy.name))

    def defense(self, attack):
        """Defense method"""
        self.hp -= attack


hero = Hero("Ethoniel", 150)
orc = Enemy("Orc", 100)

while hero.hp > 0 and orc.hp > 0:
    print("\nDostępne opcje:\n- walka\n- ucieczka\n")
    option = input("> ")

    if option == "walks":
        hero.attack(orc)
        if orc.hp <= 0:
            hero.is_win = True
            break
    elif option == "ucieczka":
        print("\nUciekasz z pola walki!")
        break
    else:
        hero.attack(orc)
        if orc.hp <= 0:
            hero.is_win = True
            break

    orc.attack(hero)
    if hero.hp <= 0:
        orc.is_win = True
        break

if hero.is_win:
    print("\nZwyciężył %s!" % hero.name)
elif orc.is_win:
    print("\nZwyciężył %s!" % orc.race)
else:
    print("\nWalka jest nierozstrzygnięta!")