# Pobieranie przedmiotów

inventory = tuple(input("Co chcesz dodać do swojego ekwipunku? (elementy dodajemy po przecinku) ").split(","))

for item in inventory:
    print(item)