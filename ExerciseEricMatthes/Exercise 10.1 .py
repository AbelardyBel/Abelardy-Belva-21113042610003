
from pathlib import Path

nama_file = Path(__file__).with_name("learning_python.txt")

print("--- Membaca seluruh file sekaligus ---")
with open(nama_file, encoding="utf-8") as file:
    isi = file.read()
print(isi)

print("--- Membaca baris demi baris dari list ---")
with open(nama_file, encoding="utf-8") as file:
    baris_baris = file.readlines()
for baris in baris_baris:
    print(baris.rstrip())
