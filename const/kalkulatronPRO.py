k1 = input("Podaj 1 liczbę: ")
k1 = int(k1)
k2 = input("Podaj 2 liczbę: ")
k2 = int(k2)

k3 = input("Jakie działanie chcesz zrobić, wpisz znak: +, -, *, /, ^, % ")
if k3 == "+":
    print("Po dodaniu wynik to: ",k1+k2)
elif k3 == "-":
    print("Po odjęciu wynik to: ",k1-k2)
elif k3 == "*":
    print("Po przemnożeniu wynik to: ",k1*k2)
elif k3 == "/":
    print("Po dzieleniu wynik to: ",k1/k2)
elif k3 == "^":
    print("Po spotęgowaniu liczby wynik to: ",k1**k2)
elif k3 == "%":
    print("Po podzieleniu reszta to: ",k1%k2)
else:
    print("Wpisz dobry znak przyjacielu")