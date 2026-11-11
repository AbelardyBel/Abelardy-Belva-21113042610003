
import json

nama = input("Siapa namamu? ")
kota = input("Kamu tinggal di kota apa? ")
hobi = input("Apa hobimu? ")

info_pengguna = {
    "nama": nama,
    "kota": kota,
    "hobi": hobi,
}

with open("user_info.json", "w") as file:
    json.dump(info_pengguna, file)

with open("user_info.json") as file:
    info_tersimpan = json.load(file)

print("\n--- Yang saya ingat tentang kamu ---")
print(f"Nama: {info_tersimpan['nama']}")
print(f"Kota: {info_tersimpan['kota']}")
print(f"Hobi: {info_tersimpan['hobi']}")
