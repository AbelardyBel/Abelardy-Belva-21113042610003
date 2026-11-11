
print("Kalkulator penjumlahan (ketik 'q' untuk berhenti).")

while True:
    teks_1 = input("\nMasukkan angka pertama: ")
    if teks_1 == "q":
        break
    teks_2 = input("Masukkan angka kedua: ")
    if teks_2 == "q":
        break
    try:
        angka_1 = int(teks_1)
        angka_2 = int(teks_2)
    except ValueError:
        print("Maaf, yang kamu masukkan bukan angka. Coba lagi dengan angka.")
    else:
        print(f"Hasilnya: {angka_1 + angka_2}")
