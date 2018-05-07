# Zapisz to
# Demonstruje zapisywanie danych do pliku tekstowego

text_file=open("zapisz_to.txt","w")
lines= ["Wiersz 1 \n", "Wiersz 2 \n","Wiersz 3 \n" ]
text_file.writelines(lines)
