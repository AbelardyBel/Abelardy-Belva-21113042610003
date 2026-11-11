nama_file_list = ["cats.txt", "dogs.txt"]

for nama_file in nama_file_list:
    print(f"\n--- Isi {nama_file} ---")
    try:
        with open(nama_file) as file:
            isi = file.read()
    except FileNotFoundError:
        print(f"Maaf, file {nama_file} tidak ditemukan.")
    else:
        print(isi)