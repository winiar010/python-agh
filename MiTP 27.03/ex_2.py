# Program wuświetlający punktację oraz umożliwiający dodawanie i usuwanie wynikówużytkowników z listy

players_count = 1
scores = []

tmp_score = input("Podaj wynik (pusty wynik oznacza koniec rejestrowania wyników): ")

while tmp_score:
    scores.append(("gracz"+str(players_count), int(tmp_score)))
    players_count += 1
    tmp_score = input("Podaj wynik (pusty wynik oznacza koniec rejestrowania wyników): ")

print("\nNick\tWynik")
for i in range(len(scores)):
    name, score = scores[i]
print("%s\t%s" % (name, score))