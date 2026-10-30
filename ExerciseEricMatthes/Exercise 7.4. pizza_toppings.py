prompt = "\nMasukkan topping pizza yang Anda inginkan:"
prompt += "\n(Ketik 'quit' untuk selesai.) "
while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizza Anda.")