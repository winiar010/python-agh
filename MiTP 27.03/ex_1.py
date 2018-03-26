# Wyświetlanie posortowanej listy wprowadzonej przez użytkownika

scores = []
score = input("Podaj wynik (pusty wynik oznacza koniec rejestrowania wyników): ")

while score:
    scores.append(int(score))
    score = input("Podaj wynik (pusty wynik oznacza koniec rejestrowania wyników): ")

scores.sort()

print("\nWyniki:", end=' ')
for i in range(len(scores)):
    print(scores[i], end=' ')

scores.sort(reverse=True)

print("\nWyniki odwrotnie:", end=' ')
for i in range(len(scores)):
    print(scores[i], end=' ')