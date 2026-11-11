from random import choice

kemungkinan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
tiket_menang = []

for _ in range(4):
    tiket_menang.append(choice(kemungkinan))

print(f"Tiket yang menang adalah {tiket_menang}.")
print("Tiket apa pun yang cocok dengan 4 angka atau huruf ini memenangkan hadiah!")
