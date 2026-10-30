kota = {
    "Solo": {
        "country": "Indonesia",
        "population": 522_000,
        "fact": "Kota kelahiran batik dan kuliner tradisional Jawa.",
    },
    "Yogyakarta": {
        "country": "Indonesia",
        "population": 373_000,
        "fact": "Kota pelajar dan pusat budaya Jawa.",
    },
    "Kyoto": {
        "country": "Jepang",
        "population": 1_460_000,
        "fact": "Terkenal dengan kuil dan bunga sakura.",
    },
}
for nama_kota, info in kota.items():
    print(f"\n{nama_kota}:")
    print(f"\tNegara: {info['country']}")
    print(f"\tPopulasi: {info['population']}")
    print(f"\tFakta: {info['fact']}")