#Obliczamy silnię

x=int(input("Podaj liczbe do obliczenia silni: "))
i=1
silnia = 1
if x>=0:
    for w in range(x):
        silnia= silnia*i
        i=i+1
    print (silnia)

elif x==1:
    print("silnia z podanej liczby = 1")

else:
    print("Podaj dodatnią liczbę > 1")
