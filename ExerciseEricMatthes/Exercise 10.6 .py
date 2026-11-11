

try:
    angka_1 = int(input("Masukkan angka pertama: "))
    angka_2 = int(input("Masukkan angka kedua: "))
    print(f"Hasilnya: {angka_1 + angka_2}")
except ValueError:
    print("Maaf, yang kamu masukkan bukan angka. Coba lagi dengan angka.")
