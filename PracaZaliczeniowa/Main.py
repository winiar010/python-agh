import linecache
import sys
import time
import datetime
import os


# PROCEDURY GLOWNE
# ======================================================================================================================
def start():
    # wyswietla ekran startowy gry
    os.system("cls")
    fileName = getConfigFileName('title')           # odczytuje lokalizacje pliku title.txt

    ileLinii = 12                                   # pierwsze 12 linii pliku title.txt to komunikat powitalny gry
    for i in range(1, ileLinii, 1):
        wiersz = getLine(fileName, i).replace("\n", "")
        print(wiersz)
        if i < 7:                                   # nazwa gry wyswietlana jest w sposob spowolniony
            time.sleep(0.3)

def dispUsers():
    # wyswietla liste userow
    getUserList()                                   # odczytuje listy userow z pliku results.txt
    #wyswietlenie listy uzytkownikow (ekran powitalny)
    lp = 1                                          # numer 1 to 'nowy gracz'
    for user in userLst:                            # wyswietla liste pozostalych graczy jesli ich lista jest w pliku results.txt
        lp = lp + 1
        print("                             " + str(lp) + ". " + userLst[user])

def getName():
    #odczytywanie nazwy nowego gracza

    opt = input("\n Wybrałem opcję: ")

    if opt == "1":                                  # nowy gracz
        userCurrent = input("Podaj swoje imie (lub nick): ")
        print("Witaj " + userCurrent + " !!! \n")
        newUserWelcomeMsg(userCurrent)              # wyswietla menu powitalne dla nowego gracza

    if int(opt) > 1:                                # stary (powracajacy) gracz
        userCurrent = userLst[int(opt) - 1]
        print("Witaj " + userCurrent)
        UidLastResult = results[int(opt) - 1]
        print("Twój ostatni wynik to : " + UidLastResult)
        existingUserWelcomeMsg(userCurrent,0)

def newUserWelcomeMsg(userCurrent):
    # wyswietla komunikat powitalny dla nowego gracza

    os.system("cls")                                    # czysci ekran konsoli
    fileName = getConfigFileName('title')               # odczytuje lokalizacje pliku title.txt

    for i in range(12, 28, 1):                          # wyswietla komunikat powitalny i reguly gry dla nowego gracza
        wiersz = getLine(fileName, i).replace("\n", "")
        print(wiersz)

    opt = input("Co wybierasz?: ")
    opt.lower()
    if opt == "q":                        # wybrano zakonczenie programu
        print("Do nastepnego razu :-(")
        sys.exit(0)

    addNewUser(userCurrent)                             # dodaje nowe gracza do listy (userLst i results)
    saveUserList()  # zapisuje wyniki wszystkich graczy do pliku results.txt
    runEx(userCurrent, 1)                               # uruchamia zadanie numer 1


def existingUserWelcomeMsg(userCurrent, option):
    # wyswietla komunikat powitalny dla 'starego' gracza

    fileName = getConfigFileName('title')                   # odczytuje lokalizacje pliku title.txt

    if option == 0:                                         # wyswietla komentarz dla istniejacego gracza (ponowne uruchomienie)
        os.system("cls")
        for i in range(29, 35, 1):
            wiersz = getLine(fileName, i).replace("\n", "")
            print(wiersz)
    elif option == 1:                                       # wyswietla komentarz dla gracza powracajacego z innego poziomu
        os.system("cls")
        for i in range(45, 50, 1):
            wiersz = getLine(fileName, i).replace("\n", "")
            print(wiersz)

    dispGameList(userCurrent)                               # odczytuje liste gier gracza

    for i in range(37, 41, 1):                              # wyswietla liste opcji (New, Quit)
        wiersz = getLine(fileName, i).replace("\n", "")
        print(wiersz)

    opt = input("Co wybierasz?: ")
    opt.lower()
    if opt == "n":                            # obsluga opcji - rozpoczynamy od nowa
        print("Rozpoczynamy wiec od zadania numer 1")
        runEx(userCurrent,1)
    elif opt == "q":                            # wybrano zakonczenie programu
        print("Do nastepnego razu :-(")
        sys.exit()
    else:
        print("Wprowadź N lub Q")

    if validLevel(opt) == 1:                                # sprawdza, do jakich poziomow gracz ma dostep
        runEx(userCurrent,opt)


def runEx(userCurrent,gameCurrentId):
    # wywolaj okreslone zadanie

    if int(gameCurrentId) < 10:                             # formatowanie numeru zadania (dla 1 >> 01, itd)
        gameCurrentId = "0" + str(gameCurrentId)

    fileName = getDirName('ex')                             # odczytuje lokalizacje katalogu z grami
    fileName = fileName + "ex" + str(gameCurrentId) + ".txt"

    os.system("cls")                                         # czysci ekran konsoli
    for i in range(1, 10, 1):                                # prezentuje graczowi reguly gry
        wiersz = getLine(fileName, i).replace("\n", "")
        if ((len(wiersz) > 0) and (wiersz[0] != "$") and (wiersz[0] != "%")):
            print(wiersz)
    opt = input("Nacisnij dowolny klawisz, aby rozpoczac \n")

    gameCurrentStartTime = getCurrentTime()                     # zapamietuje czas rozpoczecia rozwiazywania zagadki

    for i in range(11, 20, 1):                                  # prezentuje graczowi tresc zagadki
        wiersz = getLine(fileName, i).replace("\n", "")
        if ((len(wiersz) > 0) and (wiersz[0] != "$") and (wiersz[0] != "%")):  #pomijamy wiersze techniczne
            print(wiersz)
    opt = input("\n Nacisnij dowolny klawisz, gdy bedziesz gotowy do udzielenia odpowiedzi \n")

    gameCurrentDuration = getElapsedTime(gameCurrentStartTime)  # wylicza czas trwania rozwiazywania zadania (w sekundach)

    linia = linecache.getline(fileName, 2)
    answer = input("Podaj odpowiedz: ")

    while answer != linia[1:-1]:                                # sprawdza poprawność odpowiedzi
        print("Podaj poprawną odpowiedź")
        answer = input("Spróbuj jeszcze raz: ")
        if answer == linia[1:-1]:
            break
    print("Poprawna odpowiedz!")
    gameParam = getGameParam(fileName)                          # odczytuje parametry gry

    points = getCurrentResult(gameParam, gameCurrentDuration, answer) # wylicza ilosc punktow

    print("Twoj czas (w sekundach) to: " + str(gameCurrentDuration))
    print("Twoj wynik (w punktach) to: " + str(points))

    saveToResult(userCurrent,gameCurrentId,points)              # zapisuje wynik gracza do zmiennej results
    saveUserList()                                              # zapisuje wyniki wszystkich graczy do pliku results.txt

    opt = input("\n\n Nacisnij dowolny klawisz, aby kontynuowac \n")

    existingUserWelcomeMsg(userCurrent,1)                       # wyswietla menu z lista gier




# FUNKCJE POMOCNICZE
# ======================================================================================================================
def ile_recordow(fileName):
    # zlicza rekordy w pliku
    return len(open(fileName,'rU').readline()) - 1

def getLine(fileName,lineNo):
    # odczytuje konkretny wiersz z pliku
    return linecache.getline(fileName,lineNo)


def dispGameList(userId):
    #wyswietla liste gier
    userAllResults = []                                     # inicjowanie tabeli z wynikami gracza
    lp = 0                                                  # inicjowanie licznika gier

    gameDir = getDirName('ex')                              # odczytuje nazwe katalogu z plikami gier
    gameFileList = getFileList(getDirName('ex'))            # odczytuje liste plikow z grami

    if userId != "":
        userAllResults = getUserGames(userId)               # odczytywanie wynikow gracza dla wszystkich gier (results.txt)
                                                            # userALL..-gry dla danego użytkownika
    for gameFile in gameFileList:                           # odczytywanie parametrow gier wyliczamy gry z folderu z grami
        gameParam = getGameParam(gameDir + gameFile)        # Dir odczytuje lokalizację pliku
        for gameDet in gameParam:
            lp = lp + 1
            gameSplit = gameDet.split(":")
            disp = str(lp) + '. ' + gameSplit[0]
            if len(userAllResults) < lp:                    # if ilś elem użytkownika < liczby gier,
                userAllResults.append('')                   # dostawiam wart pustą
            if ((len(userAllResults) != 0) and (userAllResults[lp-1] != '')):          # dodawanie infromacji o wynikach gier juz 'granych'
                disp = disp.ljust(30," ") + " \t \t << tu juz byles - wynik: " + userAllResults[lp-1]
            print(disp)                                     # wyswietlenie listy gier

def getGameParam(fileName):
    # odczytuje parametry zadania (nazwe i rozwiazanie)
    retVal = []                                             # wyniki gry
    if os.path.isfile(fileName):                            # sprawdza, czy istnieje plik
        with open(fileName, "r") as sTxt:                   # otwiera plik do odczytu
            for wiersz in sTxt:                             # przegląda kolejne linie pliku
                if ((len(wiersz) > 0) and (wiersz[0] == "%")):
                    gameId = wiersz[1:99].replace("\n", "") # nazwa gry
                if ((len(wiersz) > 0) and (wiersz[0] == "$")):
                    gameKey = wiersz[1:99].replace("\n", "") # klucz (rozwiazanie) zadania
            retVal.append(gameId + ':' + gameKey)
    return retVal


def getUserList():
    #odczytuje liste uzytkownikow z pliku
    lp = 0
    fileName = getConfigFileName('results')                 # odczytuje lokalizacje pliku results.txt
    if os.path.isfile(fileName):                            # sprawdza, czy istnieje plik
        with open(fileName, "r") as sTxt:                   # otwiera plik do odczytu
            for line in sTxt:                               # przegląda kolejne linie pliku
                if line.replace(" ","") == '':
                    break
                t = line.split(":")                         # rozbija linię skladowe (kolumny)
                lp = lp + 1                                 # inkrementuje indeks dla tabel
                userLst[lp] = t[0]                          # dodaje nazwe gracza do tabeli userLst
                results[lp] = t[1].replace("\n", "")        # dodaje wynik gracza do rabeli results
                gameId = 0
                for game in range(2,len(t),1):
                    gameId= gameId + 1
                    resultsGame[lp,gameId] = t[game].replace("\n", "")

def saveUserList():
    #zapisuje liste uzytkownikow i ich wyniki do pliku
    fileName = getConfigFileName('results')                 # odczytuje lokalizacje pliku results.txt
    file1 = open(fileName, "w")                             # otwiera plik do zapisu, istniejący plik zostanie nadpisany(!)
    for user in userLst:
        linia = str(userLst[user]) + ":" + str(results[user])
        linia2 = ''
        for game in resultsGame:
            if game[0] == user:
                linia2 = linia2 + ":" + str(resultsGame[game])
        linia = linia + linia2 + "\n"
        #print(linia)
        file1.write(linia)                                  # zapisuje do pliku dane o wynikach
    file1.close()                                           # zamyka plik

def getUserGames(userId):
    #odczytuje z pliku results.txt dotychczasowe wyniki gracza
    fileName = getConfigFileName('results')                 # odczytuje lokalizacje pliku results.txt
    if os.path.isfile(fileName):                            # sprawdza, czy istnieje plik
        with open(fileName, "r") as sTxt:                   # otwiera plik do odczytu, otwiera plik z zabezpieczeniem
            for line in sTxt:                               # przegląda kolejne linie pliku
                t = line.split(":")                         # rozbija linię skladowe (kolumny)
                if t[0] == userId:                          # weryfikuje id gracza (nazwa,suma,wyniki..)
                    for i in range(len(t)):                 # przeglada wyniki gracza odczytane z pliku
                        if i > 1:                           # wyniki zapisane sa w kolumnach od 2 do n
                            userAllResults.append(t[i].replace("\n", ""))    # dodaje wyniki gracza do tabeli globalnej
    return userAllResults                                   # zwraca tablicę z wynikami gier od 3 kolumny

def saveToResult(userCurrent,gameCurrentId,points):
    for user in userLst:
        if userLst[int(user)] == userCurrent:
            tot = (int(results[int(user)]) + int(points))
            results[int(user)] = tot
            resultsGame[int(user),int(gameCurrentId)] = points

def addNewUser(userId):
    lp = 0
    for user in userLst:
        lp = lp + 1
    userLst[lp+1] = userId
    results[lp+1] = 0

def getCurrentTime():
    #zwraca biezaca godzine
    return datetime.datetime.now()

def getElapsedTime(startTime):
    #zwraca ile sekund uplynelo od zadanej godziny
    elapsed = getCurrentTime() - startTime
    return int(datetime.timedelta.total_seconds(elapsed))


def getConfigFileName(option):
    """
    zwraca nazwę plikow konfiguracyjnych
      INPUT:
        option - rodzaj pliku konfiguracyjnego
                results - plik z lista graczy i ich wynikami
                title   - plik z komentarzami do gry
                ex      - pliki z zadaniami
    """
    retVal = os.getcwd()       #odczytuje nazwe biezacego katalogu (z ktorego uruchomiono program)
    if option == 'results':    #katalog z plikiem dotychczasowych graczy i ich wynikow
        retVal = retVal + "/properties/results.txt"
    elif option == 'title':    #katalog z komunikatami wyswietlanymi w czasie gry
        retVal = retVal + "/properties/title.txt"
    elif option == 'ex':       #katalog z plikami z zadaniami (grami)
         retVal = retVal + "/extensions/ex1.txt"
    return retVal

def getDirName(option):
    #zwraca nazwę katalogow
    retVal = os.getcwd()       #odczytuje nazwe biezacego katalogu (z ktorego uruchomiono program)
    if option == 'results':    #katalog z plikiem dotychczasowych graczy i ich wynikow
        retVal = retVal + "/properties/"
    elif option == 'title':    #katalog z komunikatami wyswietlanymi w czasie gry
        retVal = retVal + "/properties/"
    elif option == 'ex':       #katalog z plikami z zadaniami (grami)
         retVal = retVal + "/extensions/"
    return retVal

def getFileList(directory):
    #odczytuje liste plikow w danym katalogu
    retVal = []
    #return os.listdir(directory)
    for fileName in os.listdir(directory):
        if os.path.isfile(directory + fileName):
            retVal.append(fileName)
    return retVal

def validLevel(option):
    #weryfikuje, czy wybbrany nr zadania jest poprawny

    return 1

def getCurrentResult(gameParam,gameDuration,userAnswer):
    '''
    wylicza wynik (liczbe punktow) dla danego zadania

    :param gameParam: identykator gry i klucz do rozwiazania
    :param gameDuration: czas przygotowania rozwiazania przez uzytkownika
    :param userAnswer:  odpowiedz (rozwiazanie zagadki) dostarczone przez uzytkownika

    :return: points based on time and error numbers
    '''
    retVal = 100                                    # maksymalna liczba pkt za zadanie
    t = str(gameParam).split(":")                   # z parametrow gry odczytujemy prawidlowa odpowiedz
    gameResult = t[1].replace("']","")              # w liście wyników results.txt zamieniamy

    # korygowanie ilosci punktow poprzez kontrole jakosci odpowiedzi
    userAnswer = userAnswer.replace(" ", "")         # z odpowiedzi gracza usuwa spacje
    if userAnswer.replace(" ", "") == '':              # gracz nie udzielil zadnej odpowiedzi  >> wynik 0
        retVal = 0

    if gameResult != userAnswer:                    # odp prawidlowa jest inna niz odpowiedz gracza
        for i in range(1,len(str(gameResult))):     # porownujemy kazdy element odpowiedzi gracza z odp prawidlowa
            if gameResult[i] != userAnswer[i]:
                retVal = retVal - 10                # za kazda bledna odpowiedz odejmujemy 10 pkt

    if retVal < 0:                                  # po odjeciu pkt za bledne odpowiedzi wynik jest ujemny
        retVal = 0                                  # w takim przypadku ustawiamy go na 0

    if retVal > 0:                                  # dalsza kontrola ma sens jesli dotychczasowy wynik jest dodatni
        # korygowanie ilosci punktow o czas jaki zajelo rozwiazanie
        spentTime = gameDuration - 4                # od czasu wykorzystanego odejmujemy 4 sekundy
        if spentTime > 0:                           # jesli rozwiazanie zajelo wiecej niz 4 sekundy
            retVal = retVal - (spentTime*10)        # odejmujemy 10 pkt za kazda sekunde ponad 4 s
    if retVal<0:                                    # nie pozwalamy aby wynik byl ujemny
        retVal = 0

    return retVal

# PROGRAM GLOWNY

#zmienne 'globalne'
userCurrentResult = 0               # biezacy wynik aktualnego gracza
userAllResults = []                 # tabela z dotychczasowymi parametrami gracza
userCurrent = ''                    # nick aktualnego gracza
gameCurrentId = 1                   # identyfikator biezacej gry
gameCurrentPoints = 0               # liczba punktow biezacej gry
userLst = {}                        # słownik z graczami (nicks)
results = {}                        # słownik z wynikami graczy
resultsGame = {}                    # słownik z wynikami poszczegolnych gier

# glowne procedury gry

start()                             # wyswietla komunkat powitalny
dispUsers()                         # wyswietla liste graczy (dotychczasowych)
getName()                           # wyswietla menu dla gracza (wybor) gry



#SMIETNIK

#klasy
#class Users:
    #klasa do obslugi graczy i ich rezultatow

 #   def __init__(self):
 #       self.user = []

#  def getFromFile(self):
#        # odczytywanie z pliku danych o graczach
#        dir = os.getcwd()
#        fileName = dir + "/properties/results.txt"
#        users = []
#        userNo = 0
#        ileLinii = ile_recordow(fileName)
#        for i in range(1, ileLinii, 1):
#            wiersz = getLine(fileName, i)
#            if wiersz[0:5] == "#user":
#                userNo = userNo + 1
#                print(userNo)
#                #users[userNo] = "imie:" + wiersz[8:99] + "%"
#                print("dodalem usera")
#            #for elem in enumerate(users):
#            #    print("elem")
#            # print("Linia %d: %s" %(i,wiersz))
