def make_shirt(size="L", text="Saya suka Python!"):
    """Menampilkan ringkasan kaos yang dibuat."""
    print(f"\nUkuran kaos: {size}")
    print(f'Pesan di kaos: "{text}"')


make_shirt()
make_shirt(size="M")
make_shirt(size="S", text="Belajar Python itu seru!")