#3 liczby całkowite

def silnia(liczba):
    liczba = int(liczba)
    if ((liczba == 0) or (liczba == 1)): return 1
    return silnia(liczba-1)*liczba


liczby = input("podaj 3 liczby całkowite rozdzielone przecinkiem: ")

tablica =[]
for cyfra in liczby:
    if cyfra != ",":
        print("Wprowadzono %s pozostało %s" % (cyfra,(3-int(cyfra))))

        tablica.append(int(cyfra))

        print(tablica)

print(silnia(tablica[0]))