class Car:
    """Mewakili sebuah mobil sederhana."""

    def __init__(self, make, model, year):
        """Inisialisasi atribut untuk mendeskripsikan mobil."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Mengembalikan nama deskriptif mobil yang rapi."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Menampilkan pernyataan tentang jarak tempuh mobil."""
        print(f"Mobil ini sudah menempuh {self.odometer_reading} mil.")

    def update_odometer(self, mileage):
        """Mengatur jarak tempuh ke nilai yang diberikan."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Jarak tempuh tidak bisa diputar balik!")

    def increment_odometer(self, miles):
        """Menambah jarak tempuh mobil."""
        self.odometer_reading += miles


class Battery:
    """Mewakili baterai mobil listrik."""

    def __init__(self, battery_size=40):
        """Inisialisasi atribut baterai."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Menampilkan pernyataan tentang ukuran baterai."""
        print(f"Mobil ini memakai baterai {self.battery_size}-kWh.")

    def get_range(self):
        """Menampilkan pernyataan tentang jarak tempuh baterai ini."""
        if self.battery_size == 40:
            jarak = 150
        elif self.battery_size == 65:
            jarak = 225

        print(f"Mobil ini bisa menempuh sekitar {jarak} mil dengan sekali isi daya penuh.")

    def upgrade_battery(self):
        """Menaikkan kapasitas baterai menjadi 65 kWh kalau belum 65."""
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Mewakili aspek mobil, khusus untuk kendaraan listrik."""

    def __init__(self, make, model, year):
        """Inisialisasi atribut kelas induk, lalu atribut mobil listrik."""
        super().__init__(make, model, year)
        self.battery = Battery()


mobil_listrik = ElectricCar("nissan", "leaf", 2024)
print(mobil_listrik.get_descriptive_name())
mobil_listrik.battery.describe_battery()
mobil_listrik.battery.get_range()

mobil_listrik.battery.upgrade_battery()
mobil_listrik.battery.describe_battery()
mobil_listrik.battery.get_range()
