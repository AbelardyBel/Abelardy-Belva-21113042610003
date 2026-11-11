from random import choice

kemungkinan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
tiket_saya = [3, 7, "a", "d"]

percobaan = 0
menang = False

while not menang:
    undian = []
    for _ in range(4):
        undian.append(choice(kemungkinan))
    percobaan += 1
    if undian == tiket_saya:
        menang = True

print(f"Tiket saya: {tiket_saya}")
print(f"Butuh {percobaan} kali undian sampai tiket saya menang!")
