import linecache
import time
import sys

def start():
#ekran startowy
    # odczytywanie danych z pliku
    fileName = "D:/miki/python/PracaZaliczeniowa/txtFiles/title.txt"

    # ileLinii = ile_recordow(fileName)
    ileLinii = 12
    for i in range(1, ileLinii, 1):
        wiersz = getLine(fileName, i).replace("\n", "")
        # print("Linia %d: %s" %(i,wiersz))
        print(wiersz)
        if i < 7:
            time.sleep(0.5)
def getName():
    #odczytywanie nazwy uczestnika

    opt = input("\n Wybrałem opcję: ")

    if opt == "1":
        Uid = input("Podaj swoje imie (lub nick): ")
        print("Witaj " + Uid + " !!! \n")

def welcomeMsg():
# odczytywanie danych z pliku
    fileName = "D:/miki/python/PracaZaliczeniowa/txtFiles/title.txt"

    for i in range(12, 28, 1):
        wiersz = getLine(fileName, i).replace("\n", "")
        #print("Linia %d: %s" % (i, wiersz))
        print(wiersz)

    opt = input("Co wybierasz?: ")
    if opt == "Q" or opt == "q":
        print("Do nastepnego razu :-(")
        sys.exit(0)

def dispEx1():
#zadanie 1
    fileName = "D:/miki/python/PracaZaliczeniowa/txtFiles/ex1.txt"

    for i in range(1, 18, 1):
        wiersz = getLine(fileName, i).replace("\n", "")
        #print("Linia %d: %s" % (i, wiersz))
        if ((len(wiersz) > 0) and (wiersz[0] != "$")):
            print(wiersz)
    opt = input("Nacisnij dowolny klawisz, gdy zapamietasz sekwencje klawiszy prowadzacych do wyjscia")


# FUNKCJE POMOCNICZE

#zliczanie rekordów w pliku
def ile_recordow(fileName):
    return len(open(fileName,'rU').readline()) - 1

#odczytaj konkretny wiersz z pliku
def getLine(fileName,lineNo):
    return linecache.getline(fileName,lineNo)


start()
getName()
welcomeMsg()
dispEx1()
