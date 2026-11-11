class Restaurant:
    """Mewakili sebuah restoran sederhana."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi nama restoran dan jenis masakannya."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Menampilkan deskripsi restoran."""
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.restaurant_name} sekarang buka!")

    def set_number_served(self, number):
        """Mengatur jumlah pelanggan yang sudah dilayani."""
        self.number_served = number

    def increment_number_served(self, number):
        """Menambah jumlah pelanggan yang sudah dilayani."""
        self.number_served += number


class IceCreamStand(Restaurant):
    """Mewakili kedai es krim, jenis restoran tertentu."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Inisialisasi kedai es krim beserta daftar rasanya."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        """Menampilkan daftar rasa es krim yang tersedia."""
        print(f"Rasa es krim di {self.restaurant_name}:")
        for rasa in self.flavors:
            print(f"- {rasa}")


kedai = IceCreamStand(
    "Es Krim Masuk Akal", "es krim",
    ["cokelat", "vanila", "stroberi", "matcha"],
)
kedai.describe_restaurant()
kedai.show_flavors()
