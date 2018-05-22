#5 lokacji do wyboru

class Lokacja(object):

    def __init__(self, map):
        self.map = map
        self.north = "północ"
        self.east = "zachód"
        self.west = "wschód"
        self.south = "południe"

    miejsce = input("wybierz lokację: ")

    my_location = input("Podaj lokacje: ")
    def Location(selfself, my_location):
        print(my_location)
        if my_location == "east":
            print("Wybrałeś mądrze...")
        elif my_location == "west":
            print("Wybrałeś mądrze...")
        elif my_location == "north":
            print("Wybrałeś mądrze...")
        elif my_location == "south":
            print("Wybrałeś mądrze...")
        else:
            print("nie ma takiej lokcji")

east = Lokacja()
west = Lokacja()
north = Lokacja()
south = Lokacja()
my_location = input("wybierz swoją lokację docelową: ")




