import os
import time
import linecache

#FUNKCJE
#czy plik istnieje
def plik_istnieje(fileName):
    return os.path.exists(fileName)

def rozmiar(path):
    return os.path.getsize(path)

#zliczanie rekordów w pliku
def ile_recordow(fileName):
    return len(open(fileName,'rU').readline()) - 1

#odczytaj konkretny wiersz z pliku
def getLine(fileName,lineNo):
    return linecache.getline(fileName,lineNo)

#data/godzina utworzenia
def utworzony(fileName):
    return time.ctime(os.path.getctime(fileName))

#data/godzina ostatniej modyfikacji
def modyfikowany(fileName):
    return time.ctime(os.path.getmtime(fileName))

#proby klasy os
#czy istnieje plik/katalog
print(os.path.exists("D:/Python/AA_files/"))
#lista plików w katalogu
print(os.listdir("D:/Python/"))
#odczytaj rozmiar
print(os.path.getsize("D:/Python/"))

#zapis do pliku
fileName = "D:/Python/AA_files/scratch_1.txt"
file = open(fileName,"w",-1,"utf-8")
file.write("dane1\n")
file.write("dane3\n")
file.writelines("dane2\n")
file.write("dane4\n")
file.close()

#odczytaj czas utworzenia
print(time.ctime(os.path.getctime(fileName)))
#odczytaj czas ostatniej modyfikacji
print(time.ctime(os.path.getmtime(fileName)))

#odczytywanie danych z pliku
plik = open(fileName)
try:
    text = plik.read()
finally:
    plik.close()
print(text)
print("Ilość wierszy w pliku %s: %d" %(fileName,ile_recordow(fileName)))


#odczytywanie kolejnych linii z pliku
tablica = []
ileLinii = ile_recordow(fileName)
for i in range(1,ileLinii,1):
    wiersz = getLine(fileName,i).replace("\n","")
    print("Linia %d: %s" %(i,wiersz))
    tablica.append(wiersz)
print(str(tablica))

print("Rozmiar pliku %s: %d" %(fileName,rozmiar(fileName)))