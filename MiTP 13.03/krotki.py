# Inwentarz bohatera
# Demonstruje tworzenie krotek

# utwórz pustą krotkę
inventory = ()

# potraktuj krotkę jako warunek
if not inventory:
    print("Masz puste ręce.")

input("\nAby kontynuować misję, naciśnij klawisz Enter.")

# utwórz krotkę zawierającą pewne elementy
inventory = ("miecz",
             "zbroja",
             "tarcza",
             "napój uzdrawiający")

# wyświetl krotkę
print("\nWykaz zawartości krotki:")
print(inventory)

# wyświetl każdy element krotki
print("\nElementy Twojego wyposażenia:")
for item in inventory:
    print(item)

dodawanie = input("Co chcesz dodać do swojego ekwipunku? (elementy dodajemy po przecinku) ")
dodawanie = tuple(dodawanie.split(','))
krotka = ("nóż", "miecz", "tarcza")

krotka += dodawanie

print(krotka)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

