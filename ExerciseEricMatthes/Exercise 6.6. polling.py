bahasa_favorit = {
    "Satono": "python",
    "Tamamo": "c",
    "Oguri": "rust",
    "Gentildonna": "python",
}
yang_harus_mengisi = ["Satono", "Tamamo", "Oguri", "Gentildonna", "Festa"]
for nama in yang_harus_mengisi:
    if nama in bahasa_favorit:
        print(f"Terima kasih {nama}, kamu sudah mengisi survei.")
    else:
        print(f"Halo {nama}, silakan isi survei bahasa favoritmu.")