glosarium = {
    "string": "Serangkaian karakter yang diapit tanda kutip.",
    "list": "Kumpulan item yang tersusun dalam urutan tertentu.",
    "integer": "Bilangan bulat, tanpa bagian desimal.",
    "float": "Bilangan desimal, seperti 3,14.",
    "comment": "Catatan di dalam kode yang tidak dijalankan Python.",
    "loop": "Perulangan yang menjalankan blok kode berkali-kali.",
    "dictionary": "Kumpulan pasangan kunci-nilai.",
    "tuple": "List yang tidak bisa diubah setelah dibuat.",
    "boolean": "Nilai kebenaran, True atau False.",
    "variable": "Nama yang merujuk pada suatu nilai.",
}
for kata, arti in glosarium.items():
    print(f"{kata}:\n\t{arti}\n")