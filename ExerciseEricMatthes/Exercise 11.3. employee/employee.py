class Employee:
    """Karyawan dengan nama depan, nama belakang, dan gaji tahunan."""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        """Naikkan gaji: default 5000, atau sejumlah yang diminta."""
        self.salary += amount
