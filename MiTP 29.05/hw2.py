"""
Interakcja obiektów + dziedziczenie
"""


class Character(object):
    """Klasa postaci"""
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class Enemy(Character):
    """Klasa przeciwnika"""
    def __init__(self, name, hp, character):
        super(Enemy, self).__init__(name, hp)
        self.CHARACTER = character

    def ucieczka(self):
        """Metoda ucieczki"""
        if self.CHARACTER == "zły":
            return True
        else:
            return False


hero1 = Character("Bohater1", 300)
enemy1 = Enemy("Przeciwnik1", 300, "zły")

if enemy1.ucieczka():
    print("Przeciwnik ma zły charakter i ucieka!")
else:
    print("Walka odbywa się normalnie.")