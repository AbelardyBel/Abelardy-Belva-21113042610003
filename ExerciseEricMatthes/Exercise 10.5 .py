

print("Tulis nama tamu (ketik 'quit' untuk selesai).")

nama_tamu = []
while True:
    nama = input("Nama tamu: ")
    if nama == "quit":
        break
    nama_tamu.append(nama)

with open("guest_book.txt", "w") as file:
    for nama in nama_tamu:
        file.write(nama + "\n")

print(f"{len(nama_tamu)} nama sudah disimpan di guest_book.txt.")
