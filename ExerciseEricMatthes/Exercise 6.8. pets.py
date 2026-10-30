hewan_1 = {"jenis": "anjing", "pemilik": "Mostima"}
hewan_2 = {"jenis": "kucing", "pemilik": "Kaalsit"}
hewan_3 = {"jenis": "burung", "pemilik": "Pepe"}
pets = [hewan_1, hewan_2, hewan_3]
for hewan in pets:
    print(f"Jenis: {hewan['jenis']}")
    print(f"Pemilik: {hewan['pemilik']}\n")