class Critter(object):
    def __init__(self, name, mood):
        self.__name = name
        self.__mood = mood

    def __privat_metod(self):
        print("To jest metoda prywatna")

    @property
    def mood(self):
        return self.__mood

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("imie nie może być puste")
        else:
            self.__name = new_name
            print("Zmiana imienia powiodła się")

dog = Critter(name = "Reksio", mood = "szczesliwy")
print(dog.mood)
dog.name = "Pucek"