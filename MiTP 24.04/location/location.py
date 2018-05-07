#sprawdz czy plik istnieje

import os

def lokacja():
    uprawnienia = 1

    locationName = "las"
    sciezkaDoPliku = "las"
    sciezkaDoPliku = locationName + ".txt"

    if os.path.isfile(sciezkaDoPliku):
        print("Tak")
    else:
        if uprawnienia == 1:
            answer = input("czy chcesz stworzyć plik i dodać opis lokalizacji? ")
            if answer.lower() == "tak":
                print("Tworzę plik")
                text_file = open(sciezkaDoPliku, "w")
                lines = []
                text_location = input("Podaj opis lokacji. Kolejne linie oddzielaj od siebie ';'")
                lines = text_location.split(";")
                lines = list(lines)
                text_file.writelines(lines)
                text_file.close()

            else:
                print("Nie to nie")
        else:
            print("niestety plik nie istnieje")

lokacja()