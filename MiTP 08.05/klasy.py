#definiowanie klas

class Critter(object):
    #klasa opisująca zwierzę
    total = 0
    @staticmethod
    def status():
        print("Ogólna liczba zwierzaków wynosi", Critter.total)
    def __init__(self, name):
        print("Obiekt klasy Critter urodził się")
        self.name = name
        Critter.total += 1
    def __str__(self):
        rep = "obiekt klasy Critter: \n"
        rep += "name: " + self.name + "\n"
        return rep
    def talk(self):
        print("hau hau", self.name, "!")

dog = Critter("Reksio")
dog.talk()
print(dog.name)
dog2 = Critter("Masz")
dog2.talk(dog2.name)