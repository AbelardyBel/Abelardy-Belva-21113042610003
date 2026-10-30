tempat_favorit = {
    "Stay Gold": ["Bali", "Yogyakarta", "Bromo"],
    "Gold Ship": ["Jakarta", "Bandung"],
    "Lucky Lilaac": ["Lombok"],
}
for nama, tempat in tempat_favorit.items():
    print(f"\nTempat favorit {nama} adalah:")
    for t in tempat:
        print(f"- {t}")