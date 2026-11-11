
import json

angka_favorit = input("Berapa angka favoritmu? ")
angka_favorit = int(angka_favorit)

with open("favorite_number.json", "w") as file:
    json.dump(angka_favorit, file)

print("Angka favoritmu sudah disimpan!")
