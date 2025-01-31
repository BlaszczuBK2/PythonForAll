import random
import json

# Tworzymy macierz 8x8 z wartościami losowymi większymi od zera
macierz = [[random.randint(1, 100) for _ in range(8)] for _ in range(8)]

# Przekształcamy macierz do struktury słownika
macierz_dict = {}
for i in range(8):
    for j in range(8):
        macierz_dict[f"val_{i}_{j}"] = macierz[i][j]

# Zapisujemy wynik w formacie JSON do pliku
with open("macierz.json", "w") as json_file:
    json.dump(macierz_dict, json_file, indent=4)

print("Macierz została zapisana do pliku macierz.json")
