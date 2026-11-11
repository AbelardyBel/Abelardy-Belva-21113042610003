
nama = input("Siapa nama Anda? ")

with open("guest.txt", "w") as file:
    file.write(nama)

print(f"Halo {nama}, namamu sudah disimpan di guest.txt.")
