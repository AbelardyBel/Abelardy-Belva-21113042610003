
import json

with open("favorite_number.json") as file:
    angka_favorit = json.load(file)

print(f"Saya tahu angka favoritmu! Angkanya {angka_favorit}.")
