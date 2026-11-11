
import json


def dapatkan_username_baru():
    """Meminta username baru, menyimpannya, dan mengembalikannya."""
    username = input("Siapa namamu? ")
    nama_file = "username.json"
    with open(nama_file, "w") as file:
        json.dump(username, file)
    return username


def sapa_pengguna():
    """Menyapa pengguna dengan username yang tersimpan."""
    nama_file = "username.json"
    try:
        with open(nama_file) as file:
            username = json.load(file)
    except FileNotFoundError:
        username = dapatkan_username_baru()
        print(f"Kami akan mengingatmu saat kamu kembali, {username}!")
    else:
        jawaban = input(f"Apakah namamu {username}? (ya/tidak) ")
        if jawaban == "ya":
            print(f"Selamat datang kembali, {username}!")
        else:
            username = dapatkan_username_baru()
            print(f"Kami akan mengingatmu saat kamu kembali, {username}!")


sapa_pengguna()
