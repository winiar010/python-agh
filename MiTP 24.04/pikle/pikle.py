#zapis do pliku binarnego

import pickle, shelve

s = shelve.open("pikle2.dat")
s["odmiana"] = ["łagodny", "pikanty", "kwaszony"]
s["kształt"] = ["krojony", "cały", "w plasterkach"]
s["marka"] = ["marka 1", "marka 2", "marka 3"]
s.sync()

print ("Pobieranie informacji z półek")

print("marka - ", s["marka"])
print("kształt - ", s["kształt"])
print("odmiana - ", s["odmiana"])
s.close()