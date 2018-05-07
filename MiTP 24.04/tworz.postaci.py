#zapis do pliku binarnego

import pickle, shelve

print("Konserwowanie list")
variety = ["łagodny", "pikantny", "kwaszony"]
shape = ["cały", "Krojony wzdłuż", "w plasterkach"]
brand = ["Klimex", "Pol", "Daytona"]

f = open("piklel.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

f = open("piklel.dat", "rb")
variety1 = pickle.load(f)
shape1 = pickle.load(f)
brand1 = pickle.load(f)
print(variety1)
print(shape1)