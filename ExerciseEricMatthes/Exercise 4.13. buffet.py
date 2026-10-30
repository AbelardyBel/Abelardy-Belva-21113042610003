makanan = ("nasi goreng", "ayam geprek", "soto", "gado-gado", "rendang")
for m in makanan:
    print(m)

# Baris di bawah ini akan error kalau dihilangkan tanda #-nya,
# karena tuple tidak bisa diubah:
# makanan[0] = "mie goreng"

makanan = ("nasi goreng", "ayam geprek", "soto", "gado-gado", "sate")
print("\nMenu baru:")
for m in makanan:
    print(m)