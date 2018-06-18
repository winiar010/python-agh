#Mini gra w kości
import random
import time
import sys
import linecache

'''def start():
    fileName = "D:/miki/python/PracaZaliczeniowa/koscitxt/start.txt"
    ileLinii = 10
    for i in range(1, ileLinii, 1):
        wiersz = getLine(fileName, i).replace("\n", "")
        print(wiersz)
        if i < 7:
            time.sleep(0.5)
#odczytaj konkretny wiersz z pliku
def getLine(fileName,lineNo):
    return linecache.getline(fileName,lineNo)'''
def napis():
    text = "Zaczynamy naszą małą mini grę...\n"
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

def przywitanie():
    text = """Witaj w grze w kości 1.0...
jest to pierwsza odsłona tej gry...\n"""
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
'''def wynik():
    for i in range (37):
        two_dig = i - int(i / 100) * 100
        last_dig = i - int(i / 10) * 10
        if i in range(1, 4) and (22, 24) and (32, 34):
            print("punkty")
        else:
            print("punktów")'''
def game():
    again = 'T' or 't'
    #przywitanie()
    #napis()
    while again == 'T' or 't': #lower.
        kosci = []
        pkt = 0
        while len(kosci) < 5:
            liczba = random.randint(1, 6)
            print("Wyrzucono: ", liczba)
            kosci.append(liczba)
            pkt += liczba
        print("Wyrzuciłeś: ", kosci)
        if pkt in range (1):
            print("To jest dokładnie ", pkt, "punkt")
        elif pkt in range (1, 4) and (22, 24) and (32, 34):
            print("To są dokładnie ", pkt, "punkkty")
        else:
            print("To jest dokładnie ", pkt, "punktów")

        again = input("\nGramy jeszcze raz? (T/N)")


def menu():
    print("Co chciałbyś zrobić?")
    print("""
    1 - Zacznij nową grę
    2 - Wczytaj zapisaną grę
    3 - Pokaż najlepszy wynik
    4 - Instrukcja gry
    5 - Zabierz mnie stąd! (Wyjście)    
    """)
    selection = input("Wpisz odpowiednią cyfrę: ")
    if selection == '1':
        game()

    elif selection == '2':
        pass

    elif selection == '3':
        pass
    elif selection == '4':
        pass
    elif selection == '5':
        pass
    else:
        print("Wybierz opcję 1-5!")

#start()
menu()