from pathlib import Path

# Exercise 10.3. simpler_code.py
# Tiga program file_reader.py dari bab ini, tanpa variabel
# sementara 'lines' — loop langsung ke hasil splitlines().

nama_file = Path(__file__).with_name("learning_python.txt")

# Cara 1: membaca seluruh isi file.
print("--- Seluruh isi file ---")
with open(nama_file, encoding="utf-8") as file:
    isi = file.read()
print(isi)

# Cara 2: loop langsung ke splitlines(), tanpa variabel 'lines'.
print("--- Baris demi baris (splitlines) ---")
with open(nama_file, encoding="utf-8") as file:
    isi = file.read()
for baris in isi.splitlines():
    print(baris)

# Cara 3: membuat list baris, lalu loop — juga tanpa variabel 'lines'.
print("--- Dari list baris ---")
with open(nama_file, encoding="utf-8") as file:
    isi = file.read()
for baris in isi.splitlines():
    print(baris)
