
import json

nama_file = "favorite_number.json"

try:
    with open(nama_file) as file:
        angka_favorit = json.load(file)
except FileNotFoundError:
    angka_favorit = input("Berapa angka favoritmu? ")
    angka_favorit = int(angka_favorit)
    with open(nama_file, "w") as file:
        json.dump(angka_favorit, file)
    print("Angka favoritmu sudah disimpan!")
else:
    print(f"Saya tahu angka favoritmu! Angkanya {angka_favorit}.")
