# Perluasan dari Exercise 6.11. cities.py:
# ditambah satu kota baru (Bandung) dan satu key baru (julukan),
# serta judul tiap kota menampilkan julukannya.
kota = {
    "Solo": {
        "country": "Indonesia",
        "population": 522_000,
        "fact": "Kota kelahiran batik dan kuliner tradisional Jawa.",
        "julukan": "Kota Batik",
    },
    "Yogyakarta": {
        "country": "Indonesia",
        "population": 373_000,
        "fact": "Kota pelajar dan pusat budaya Jawa.",
        "julukan": "Kota Pelajar",
    },
    "Kyoto": {
        "country": "Jepang",
        "population": 1_460_000,
        "fact": "Terkenal dengan kuil dan bunga sakura.",
        "julukan": "Kota Seribu Kuil",
    },
    "Bandung": {
        "country": "Indonesia",
        "population": 2_470_000,
        "fact": "Dikenal sebagai Paris van Java.",
        "julukan": "Kota Kembang",
    },
}
for nama_kota, info in kota.items():
    print(f"\n{nama_kota} ({info['julukan']}):")
    print(f"\tNegara: {info['country']}")
    print(f"\tPopulasi: {info['population']}")
    print(f"\tFakta: {info['fact']}")