def make_sandwich(*items):
    """Menampilkan ringkasan sandwich yang dipesan."""
    print("\nMembuat sandwich dengan isi berikut:")
    for item in items:
        print(f"- {item}")


make_sandwich("keju")
make_sandwich("tuna", "selada")
make_sandwich("ayam", "tomat", "keju", "mayones")