from random import randint


class Die:
    """Mewakili sebuah dadu."""

    def __init__(self, sides=6):
        """Inisialisasi jumlah sisi dadu."""
        self.sides = sides

    def roll_die(self):
        """Menampilkan angka acak antara 1 dan jumlah sisi dadu."""
        print(randint(1, self.sides))


dadu_6 = Die()
print("Dadu 6 sisi:")
for _ in range(10):
    dadu_6.roll_die()

dadu_10 = Die(10)
print("\nDadu 10 sisi:")
for _ in range(10):
    dadu_10.roll_die()

dadu_20 = Die(20)
print("\nDadu 20 sisi:")
for _ in range(10):
    dadu_20.roll_die()
