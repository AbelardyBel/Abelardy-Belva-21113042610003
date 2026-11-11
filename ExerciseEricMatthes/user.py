"""Modul berisi kelas User (untuk Exercise 9-12)."""


class User:
    """Mewakili seorang pengguna."""

    def __init__(self, first_name, last_name, age, city, pekerjaan):
        """Inisialisasi data pengguna."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.pekerjaan = pekerjaan
        self.login_attempts = 0

    def describe_user(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age} tahun")
        print(f"Kota: {self.city}")
        print(f"Pekerjaan: {self.pekerjaan}")

    def greet_user(self):
        """Menampilkan sapaan personal untuk pengguna."""
        print(f"Halo {self.first_name} {self.last_name}, selamat datang!")

    def increment_login_attempts(self):
        """Menambah jumlah percobaan login sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mengatur ulang jumlah percobaan login menjadi 0."""
        self.login_attempts = 0
