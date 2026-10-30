tamu = ["Galileo Galilei", "Albert Einstein", "Charles Darwin", "Marie Curie", "Leonardo da Vinci", "Thomas Edison"]
print("Maaf, saya hanya bisa mengundang dua orang untuk makan malam.")

tamu_batal = tamu.pop()
print(f"Maaf {tamu_batal}, saya tidak bisa mengundangmu makan malam.")
tamu_batal = tamu.pop()
print(f"Maaf {tamu_batal}, saya tidak bisa mengundangmu makan malam.")
tamu_batal = tamu.pop()
print(f"Maaf {tamu_batal}, saya tidak bisa mengundangmu makan malam.")
tamu_batal = tamu.pop()
print(f"Maaf {tamu_batal}, saya tidak bisa mengundangmu makan malam.")

print(f"\nHalo {tamu[0]}, kamu tetap diundang makan malam.")
print(f"Halo {tamu[1]}, kamu tetap diundang makan malam.")

del tamu[0]
del tamu[0]
print(tamu)