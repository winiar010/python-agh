#zapis stanu gry i wczytanie stanu
import pickle, shelve
def zapis():
    f = open ("postac.dat", "wb")
    pickle.dump(nazwa, f)
    pickle.dump(poziom, f)
    pickle.dump(nazwa_lokacji, f)
    pickle.dump(numery_zad, f)
    f.close()

def odczyt():
    '''plik = open("postac.dat", "rb")
    try:
        f = plik.read() 
    finally:
        plik.close()
    print (f)'''
    print(nazwa)
    print(poziom)
    print(nazwa_lokacji)
    print(numery_zad)

print("Kreator tworzenia postaci... \n")
nazwa = input("Podaj nazwę postaci: ")
poziom = input("Podaj poziom postaci: ")
poziom = int(poziom )
nazwa_lokacji = input("Podaj nazwę lokacji postaci: ")
numery_zad = input("Podaj wykonane numery zadań: ") .split(",")

zapis()
odczyt()








