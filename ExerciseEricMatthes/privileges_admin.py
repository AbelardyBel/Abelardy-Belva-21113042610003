"""Modul berisi kelas Privileges dan Admin (untuk Exercise 9-12)."""

from user import User


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

    