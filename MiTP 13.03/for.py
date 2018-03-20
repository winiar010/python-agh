
# Licznik
# Demonstruje funkcję range()

number = 0
for number in range (0, 50, 3):
    print(number, end=" ")

print("\n\nLiczenie:")
for i in range(10):
    print(i, end=" ")

print("\n\nLiczenie co pięć:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nLiczenie do tyłu:")
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
