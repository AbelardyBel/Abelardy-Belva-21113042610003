while True:
    umur = input("Berapa umur Anda? (Ketik 'quit' untuk selesai.) ")
    if umur == "quit":
        break
    umur = int(umur)
    if umur < 3:
        print("Tiket Anda gratis.")
    elif umur <= 12:
        print("Tiket Anda 10 dolar.")
    else:
        print("Tiket Anda 15 dolar.")