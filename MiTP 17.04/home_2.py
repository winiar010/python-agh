#postać

def moce():
    dane = []
    imie = input("podaj imię postaci: ")
    wiek = input("Podaj wiek postaci: ")
    wiek = int(wiek)
    plec = input("Podaj płeć postaci: ")
    rasa = input("Podaj rasę postaci: ")
    cechy = input("Podaj cechy postaci (zwinność, budowa, siła, szybkość, inteligencja) liczbowo po przecinku: ")
    cechy = cechy.split(",")
    dane += imie, wiek, plec,rasa,cechy
    print(dane)


print("Witaj w kreatorze Twojej postaci, podaj odpowiednie dane: ")

moce()

