##1
# Kalkulator wykonujący proste działania na podstawie liczb podanych przez użytkownika

print("PROSTY KALKULATOR\n")
numbers = input("Podaj dwie liczby (odzdielone przecinkiem): ")
number1, number2 = numbers.split(",")

number1, number2 = float(number1), float(number2)

print("\nWYNIKI:\n")
print("Dodawanie:", number1+number2)
print("Odejmowanie:", number1-number2)
print("Mnożenie:", number1*number2)
if number2:
    print("Dzielenie:", number1/number2)
else:
    print("Dzielenie: Nie dziel przez 0!")

##2
# Kalkulator rozbudowany o możliwość wyboru działania, oraz o potęgowanie i modulo

print("ROZBUDOWANY KALKULATOR")

operation = ""

while True:
    print("""
MENU:
[1] - Dodawanie
[2] - Odejmowanie
[3] - Mnożenie
[4] - Dzielenie
[5] - Potęgowanie
[6] - Modulo
[0] - Wyjście
    """)

    operation = input("Wybierz działanie: ")

    if operation == "0":
        break
    elif operation == "1":
        numbers = input("Podaj liczby (oddzielone przecinkiem): ")

        number1, number2 = numbers.split(",")
        number1, number2 = float(number1), float(number2)

        print(number1, " + ", number2, " = ", number1+number2)
    elif operation == "2":
        numbers = input("Podaj liczby (oddzielone przecinkiem): ")

        number1, number2 = numbers.split(",")
        number1, number2 = float(number1), float(number2)

        print(number1, " - ", number2, " = ", number1-number2)
    elif operation == "3":
        numbers = input("Podaj liczby (oddzielone przecinkiem): ")

        number1, number2 = numbers.split(",")
        number1, number2 = float(number1), float(number2)

        print(number1, " * ", number2, " = ", number1*number2)
    elif operation == "4":
        numbers = input("Podaj liczby (oddzielone przecinkiem): ")

        number1, number2 = numbers.split(",")
        number1, number2 = float(number1), float(number2)

        if number2:
            print(number1, " / ", number2, " = ", number1/number2)
        else:
            print("Nie dziel przez 0!")
    elif operation == "5":
        numbers = input("Podaj liczby (oddzielone przecinkiem): ")

        number1, number2 = numbers.split(",")
        number1, number2 = float(number1), float(number2)

        print(number1, " ^ ", number2, " = ", number1**number2)
    elif operation == "6":
        numbers = input("Podaj liczby (oddzielone przecinkiem): ")

        number1, number2 = numbers.split(",")
        number1, number2 = float(number1), float(number2)

        if number2:
            print(number1, " % ", number2, " = ", number1%number2)
        else:
            print("Nie dziel przez 0!")
    else:
        print("Nieznana opcja!")

    decision = input("Chcesz kontynuować (T/n)? ")

    if decision == "T" or decision == "t":
        continue
    else:
        break

##3
# Zmodyfikowany Symulator trzylatka

print("\tWitaj w 'Symulatorze trzylatka'\n")
print("Ten program symuluje rozmowę z trzyletnim dzieckiem.")
print("Spróbuj przerwać to szaleństwo.\n")

response = ""
while response != "Dlatego.":
    response = input("Dlaczego?\n").capitalize()

print("Aha, już wiem.")

##4
# Data urodzenia oraz płeć na podstawie numeru PESEL

pesel = input("Podaj swój numer PESEL: ")

while int(len(pesel)) != 11:
    print("\nPESEL musi mieć 11 znaków!\n")
    pesel = input("Podaj swój numer PESEL: ")

# SECTION: date of birth
year = pesel[0:2]
month = pesel[2:4]
day = pesel[4:6]

if month[0] == '0' or month[0] == '1':
    year = "19" + year
elif month[0] == '2' or month[0] == '3':
    year = "20" + year
    month = int(month)
    month -= 20
    if month < 10:
        month = str(month)
        month = "0" + month
    else:
        month = str(month)
else:
    print("\nPodano błędny PESEL!\n")
    exit()

# SECTION: gender
gender_num = int(pesel[9])

if gender_num % 2 == 0:
    gender = "Kobieta"
else:
    gender = "Mężczyzna"

print("\nTwoja data urodzenia: "+day+"."+month+"."+year)
print("Twoja płeć to: "+gender)

##5
# Mini lotto
import random

template = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
drawn_numbers = []

tmp_numbers = input("Podaj trzy cyfry z zakresu 0-9 oddzielone przecinkiem: ")

number1, number2, number3 = tmp_numbers.split(",")

if number1 not in template:
    print("\nPodano cyfrę spoza zakresu!")
    exit()
if number2 not in template:
    print("\nPodano cyfrę spoza zakresu!")
    exit()
if number3 not in template:
    print("\nPodano cyfrę spoza zakresu!")
    exit()

for i in range(6):
    tmp_draw_number = str(random.randint(0, 9))

    while tmp_draw_number in drawn_numbers:
        tmp_draw_number = str(random.randint(0, 9))

    drawn_numbers.append(tmp_draw_number)

win_numbers_counter = 0

if number1 in drawn_numbers:
    win_numbers_counter += 1
if number2 in drawn_numbers:
    win_numbers_counter += 1
if number3 in drawn_numbers:
    win_numbers_counter += 1

if win_numbers_counter == 0:
    print("\nNie trafiono żadnej liczby!")
elif win_numbers_counter == 1:
    print("\nTrafiono 1 liczbę!")
elif win_numbers_counter == 2:
    print("\nTrafiono 2 liczby!")
elif win_numbers_counter == 3:
    print("\nZwycięstwo! Trafiono wszystkie 3 liczby!")
else:
    print("\nCoś poszło nie tak!")

