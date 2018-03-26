
# Program wypisujący listę słów w przypadkowej kolejności
import random

words = ["ananas", "agrest", "banan", "cytryna", "jabłko", "truskawka", "pomarańcza", "mandarynka"]
result = []

while words:
    index = random.randint(0, len(words) - 1)
    result.append(words.pop(index))

for i in range(len(result)):
    print(result[i])