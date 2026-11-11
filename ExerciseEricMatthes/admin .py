"""Modul berisi kelas User, Privileges, dan Admin (untuk Exercise 9-11)."""


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


class Privileges:
    """Mewakili hak istimewa seorang administrator."""

    def __init__(self, privileges):
        """Inisialisasi daftar hak istimewa."""
        self.privileges = privileges

    def show_privileges(self):
        """Menampilkan daftar hak istimewa."""
        print("Hak istimewa admin:")
        for hak in self.privileges:
            print(f"- {hak}")


class Admin(User):
    """Mewakili seorang administrator, jenis pengguna tertentu."""

    def __init__(self, first_name, last_name, age, city, pekerjaan):
        """Inisialisasi admin beserta hak istimewanya."""
        super().__init__(first_name, last_name, age, city, pekerjaan)
        self.privileges = Privileges([
            "can add post",
            "can delete post",
            "can ban user",
        ])
