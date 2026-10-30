pengguna_saat_ini = ["blaze", "laevatain", "bronya", "mei", "mejiro"]
pengguna_baru = ["Blaze", "Laevatain", "Zaychik", "Mei", "Orvefre"]
pengguna_saat_ini_kecil = [p.lower() for p in pengguna_saat_ini]
for nama_baru in pengguna_baru:
    if nama_baru.lower() in pengguna_saat_ini_kecil:
        print(f"Nama pengguna {nama_baru} sudah dipakai, silakan pilih nama lain.")
    else:
        print(f"Nama pengguna {nama_baru} tersedia.")