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


restaurant = Restaurant("Warung Sederhana", "masakan Jawa")
print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")

restaurant.number_served = 25
print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")

restaurant.set_number_served(40)
print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")

restaurant.increment_number_served(15)
print(f"Pelanggan yang sudah dilayani: {restaurant.number_served}")
