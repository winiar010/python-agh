# Odczytaj to
# Demonstruje odczytywanie danych z pliku tekstowego

print("Otwarcie i zamknięcie pliku.")
text_file = open("odczytaj_to.txt", "r")
text_file.close()

print("\nOdczytywanie znaków z pliku.")
text_file = open("odczytaj_to.txt", "r")
print(text_file.read(1))
print(text_file.read(7))

lines = text_file.readline()
print(len(lines))
for line in lines:
    print(line)
text_file.close()