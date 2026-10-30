prompt = "\nMasukkan topping pizza yang Anda inginkan:"
prompt += "\n(Ketik 'quit' untuk selesai.) "

# Versi 1: tes kondisional di pernyataan while
print("\n--- Versi 1: tes kondisional di while ---")
topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")

# Versi 2: variabel aktif
print("\n--- Versi 2: variabel aktif ---")
aktif = True
while aktif:
    topping = input(prompt)
    if topping == "quit":
        aktif = False
    else:
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")

# Versi 3: break
print("\n--- Versi 3: break ---")
while True:
    topping = input(prompt)
    if topping == "quit":
        break
    print(f"Saya akan menambahkan {topping} ke pizza Anda.")