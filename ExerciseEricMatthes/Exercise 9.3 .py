class User:
    """Mewakili seorang pengguna."""

    def __init__(self, first_name, last_name, age, city, pekerjaan):
        """Inisialisasi data pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.asal = city
        self.pekerjaan = pekerjaan

    def describe_user(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age} tahun")
        print(f"Kota: {self.asal}")
        print(f"Pekerjaan: {self.pekerjaan}")

    def greet_user(self):
        """Menampilkan sapaan personal untuk pengguna."""
        print(f"Halo {self.first_name} {self.last_name}, selamat datang!")


pengguna_1 = User("Kiana", "Kaslana", 20, "Honkai", "Honkai Knight")
pengguna_2 = User("Angelina", "Ajimu", 22, "Arknight", "Operator")
pengguna_3 = User("Nakayama", "Festa", 18, "Uma", "Siswa")

pengguna_1.describe_user()
pengguna_1.greet_user()
print()
pengguna_2.describe_user()
pengguna_2.greet_user()
print()
pengguna_3.describe_user()
pengguna_3.greet_user()
