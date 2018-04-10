#FUNKCJE
def instrukcja():
    # wyświetla instrukcje gry
    print(
        'Chce sprawdzić, czy wiesz co to są liczby całkowite.\n'
        'a może potrafisz podać trzy liczby pitagorejskie? \n'
        'To nie takie proste :-) \n'
    )

def czy_calkowita(liczba):
    # walidacja, czy liczba całkowita
    #print (liczba.is_integer())
    if liczba.is_integer():
        return True
    else:
        return False

def czy_liczba(liczba):
    #walidacja, czy wprowadzono liczbę
    #print (liczba.replace("1",""))
    liczba = liczba.replace("1","")
    liczba = liczba.replace("2", "")
    liczba = liczba.replace("3", "")
    liczba = liczba.replace("4", "")
    liczba = liczba.replace("5", "")
    liczba = liczba.replace("6", "")
    liczba = liczba.replace("7", "")
    liczba = liczba.replace("8", "")
    liczba = liczba.replace("9", "")
    liczba = liczba.replace("0", "")
    liczba = liczba.replace(".", "")
    if liczba == "":
        return True
    else:
        return False

def sortuj(tab):
    # sortowanie tablicy od najmniejszej wartości do największej
    for i in range(len(tab)-1,0,-1):
        for j in range(i):
            if int(tab[j]) > int(tab[j + 1]):
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    #print(str(tab))
    return tab

def sumuj(tab):

    suma = 0
    for i in range(len(tab)):
        suma = suma + int(tab[i])
    #print("\n")
    print("Suma wybranych liczb: %d \n" %suma)
    return suma

def czy_lp_pitagorejskie(tab):
    #liczby pitagorejskie spełniają warunek: a*a+b*b=c*c
    if (int(tab[0])*int(tab[0]))+(int(tab[1])*int(tab[1])) == (int(tab[2])*int(tab[2])):
        return True
    else:
        return False

def potegowanie(val, potega):
    result = val
    for i in range(1,int(potega),1):
        result = result*val
    #print(int(val))
    return result

def silnia(liczba):
    liczba = int(liczba)
    if ((liczba == 0) or (liczba == 1)): return 1
    return silnia(liczba-1)*liczba

#main
# inicjowanie zmiennych
tablica = []
nrLiczby = 1
#instrukcja gry
instrukcja()
#zaczynamy
print ("Podaj 3 liczby całkowite")

while nrLiczby < 4:
    Liczba = input("Podaj liczbę nr %s: " % nrLiczby)
    Liczba = Liczba.replace(",",".")
    if Liczba.upper() == "Q":
        print("Do następnego razu !!!")
        break
    if Liczba == "":
        print ("Coś jednak musisz wprowadzić :-). Jeśli chcesz przerwać wpisz 'Q'.")
    else:
        if czy_liczba(Liczba) == False:
            print ("Błąd. Nie wprowadziłeś liczby !!!")
        else:
            if czy_calkowita(float(Liczba)) == False:
                print ("Błąd. Podana liczba nie jest całkowita!!!")
            else:
                nrLiczby = nrLiczby + 1
                tablica.append(Liczba.replace(".",""))

# określanie co wprowadzono
disp = ""
for i in tablica:
    disp = disp + i + ";"
disp = disp[0:len(disp)-1]

# wyświetlanie wyniku
if disp != "":
    print(
        "\n"
        "Wybrałeś liczby: " + disp + "\n"
        "Jednak wiesz co to są liczby całkowite !!! \n"
    )
    sortuj(tablica)
    print("Tablica po sortowaniu od liczby najmniejszej do największej:")
    print(str(tablica))

    #suma podanych liczb
    suma = sumuj(tablica)

    #czy podano liczby pitagorejskie
    if czy_lp_pitagorejskie(tablica) == True:
        print("Gratulacje, trafiłeś liczby pitagorejskie !!! \n")
    else:
        print("Niestety to nie są liczby pitagorejskie :-( \n")

    #suma liczb do potegi 2,3,4,5
    print("Suma wprowadzonych liczb %d do potegi 2, 3, 4, 5" %int(suma))
    for i in range(2,6,1):
        print("^%d >> %d" %(i,potegowanie(suma,i)))

    #silnia dla najmniejszej z podanych liczb
    print("\n")
    print("Silnia dla liczby %s to: %s" %(tablica[0],silnia(tablica[0])))



'''
multiline
comment
'''