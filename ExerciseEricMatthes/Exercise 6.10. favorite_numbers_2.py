angka_favorit = {
    "Kianna": [7, 21],
    "Bronya": [3, 9],
    "Mei": [21, 13],
    "Himeko": [9, 5],
    "Mobius": [13, 7],
}
for nama, angka in angka_favorit.items():
    print(f"\nAngka favorit {nama} adalah:")
    for a in angka:
        print(f"- {a}")