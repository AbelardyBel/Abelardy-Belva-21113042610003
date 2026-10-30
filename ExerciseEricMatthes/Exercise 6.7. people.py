orang_1 = {"first_name": "Nakayama", "last_name": "Festa", "age": 17, "city": "Hokkaido"}
orang_2 = {"first_name": "Tosen", "last_name": "Jordan", "age": 18, "city": "Hokkaido"}
orang_3 = {"first_name": "Winning", "last_name": "Ticket", "age": 19, "city": "Shizunai"}
people = [orang_1, orang_2, orang_3]
for orang in people:
    print(f"Nama: {orang['first_name']} {orang['last_name']}")
    print(f"Umur: {orang['age']}")
    print(f"Kota: {orang['city']}\n")