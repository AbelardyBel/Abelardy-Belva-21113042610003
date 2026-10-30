responses = {}
polling_active = True
while polling_active:
    nama = input("\nSiapa nama Anda? ")
    response = input("Jika Anda bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")
    responses[nama] = response
    repeat = input("Apakah ada orang lain yang mau menjawab survei? (ya/tidak) ")
    if repeat == "tidak":
        polling_active = False
print("\n--- Hasil Survei ---")
for nama, response in responses.items():
    print(f"{nama} ingin pergi ke {response}.")