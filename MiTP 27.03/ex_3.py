# Manual


def show_manual():
    print("\nDostępne komendy:")
    for key in commands.keys():
        print("-", key)


commands = {"north": "Idź na północ",
            "south": "Idź na południe",
            "east": "Idź na wschód",
            "west": "Idź na zachód",
            "przejdź": "Przejdź przez drzwi",
            "opuść": "Wyjdź z gry",
            "manual": "Pokaż manual",
            "komenda [komenda]": "Pokaż funkcje komendy"}

show_manual()
command = input("Co chcesz zrobić? ").lower()

while command:

    if command in commands or "komenda" in command:
        if command == "manual":
            show_manual()
        elif command[:7] == "komenda":
            if command[8:] in commands:
                print("%s - %s" % (command[8:], commands[command[8:]]))
            else:
                print("Nie ma takiej komendy!")
        else:
            pass
    else:
        print("\nNiepoprawna komenda!")

    command = input("Co chcesz zrobić? ").lower()