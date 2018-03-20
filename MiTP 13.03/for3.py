krotka = ("element 1",)
krotka2 =()
tresc = input("Podaj ciąg znaków, rozdziel przecinkiem: ")
print(tresc.split(","))
krotka2 = tuple(tresc.split(" , "))


krotka += krotka2

print(krotka)