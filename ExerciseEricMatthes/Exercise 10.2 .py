from pathlib import Path



nama_file = Path(__file__).with_name("learning_python.txt")

with open(nama_file, encoding="utf-8") as file:
    for baris in file:
        baris_baru = baris.replace("Python", "C")
        print(baris_baru.rstrip())
