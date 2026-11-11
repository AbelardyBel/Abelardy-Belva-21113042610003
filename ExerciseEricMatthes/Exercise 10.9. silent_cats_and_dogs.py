
nama_file_list = ["cats.txt", "dogs.txt"]

for nama_file in nama_file_list:
    print(f"\n--- Isi {nama_file} ---")
    try:
        with open(nama_file) as file:
            isi = file.read()
    except FileNotFoundError:
        pass
    else:
        print(isi)
