#funkcja sumy


''' print("Wprowadź dwie liczby, które chcesz zsumować (po przecinku: ")
liczby = []

    def suma(liczby):
            suma = 0
        for i in liczby:
            suma = suma + i
            return suma '''
lista = [4, 5, 8, 12, 4] # lista z liczbami calkowitymi

# funkcja sumujaca elekemty listy
def my_sum(list):
        suma = 0 # zmienna przechowujaca sume
        for i in list: # petla, ktora sumuje po kolei elementy listy
                suma = suma + i

        return suma # zwaracamy zmienna

print my_sum(lista) # wyswietlamy dzialanie funkcji na ekran

