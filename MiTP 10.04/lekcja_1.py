def display():
    '''Wyświetli napis na ekranie'''
    #print("ELO")
    five = 5
    return five
#main
print(display())

def display(message):
    print(message)

#main
display("cześć, to ja!")

def birth(name = "Kasia", year = 9):
    print("cześć", name, "Wszystkiego najlepszego! z okazji ", year, "urodzin")

#main
birth(year = 7, name = "Tadek")
birth()
birth(name = "Tomek", year = 6)
birth(name = "Tadek")

