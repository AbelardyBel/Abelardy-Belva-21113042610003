
nama_file_list = ["contoh_teks_1.txt", "contoh_teks_2.txt"]

for nama_file in nama_file_list:
    try:
        with open(nama_file, encoding="utf-8") as file:
            isi = file.read()
    except FileNotFoundError:
        print(f"Maaf, file {nama_file} tidak ditemukan.")
    else:
        jumlah = isi.lower().count("the")
        print(f"Kata 'the' muncul {jumlah} kali di {nama_file}.")
