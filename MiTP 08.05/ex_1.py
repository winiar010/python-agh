#własna klasa

class Postac(object):
    '''klasa postaci'''

    def __init__(self, name):
        self.name = name
        self.rasa = "mag"
        self.hp = 500
        self.obrona = 50
        self.sila = 50
        self.zrecznosc = 50
        self.budowa = 50
        self. inteligencja = 50

    @staticmethod
    def dobadz_bron():
            print("Dobyles bron")
postac = Postac("test")
postac.dobadz_bron()






