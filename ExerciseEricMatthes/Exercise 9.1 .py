class Restaurant:
    """Mewakili sebuah restoran sederhana."""

    def __init__(self, restaurant_name, cuisine_type):
        """Inisialisasi nama restoran dan jenis masakannya."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Menampilkan deskripsi restoran."""
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        print(f"Restoran {self.restaurant_name} sekarang buka!")


restaurant = Restaurant("Warung Sederhana", "masakan Jawa")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
