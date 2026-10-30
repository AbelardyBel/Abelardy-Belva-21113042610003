def build_profile(first, last, **user_info):
    """Membuat dictionary yang berisi profil pengguna."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


profil = build_profile(
    "Abelardy",
    "Belva",
    lokasi="Solo",
    bidang="Teknik Industri",
    hobi="Kuda",
)
print(profil)