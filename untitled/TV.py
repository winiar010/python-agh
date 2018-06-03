class Telewizor(object):
    def __init__(self, volume=50, channel=1):
        self.volume = volume
        self.channel = channel

    def program(self, numer):
        self.channel = numer
        print("Wybrany kanal: ", self.channel)

    def volumeup(self):
        self.volume += 1
        if self.volume > 100:
            self.volume = 100
        print("Glosnosc: ", self.volume)

    def volumedown(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
        print("Gloscnosc: ", self.volume)


def pilot():
    tele = Telewizor()
    choice = None

    while choice != "0":
        print("""
        Witaj w pythonowej wersji telewizora!
        Wybierz jeden z przyciskow:
    0 - wylacz telewizor
    1 - zmien kanal
    2 - zwieksz glosnosc
    3 - zmniejsz glosnosc""")

        choice = input("Wpisz cyfre: ")

        if choice == "0":
            print("\nTelewizor zostal wylaczony")
        elif choice == "1":
            numer = int(input("\nWybierz kanal od 1 do 20: "))
            tele.program(numer)
            if numer > 20:
                print('Nie wykupiles pakietu ekstra! Wybierz kanal od 1 do 20!')
        elif choice == "2":
            tele.volumeup()
        elif choice == "3":
            tele.volumedown()
        else:
            print("\nNiepoprawny wybor, wybierz 0, 1, 2 lub 3.")


pilot()

input("\n\nAby zakończyć nacisnij ENTER.")
