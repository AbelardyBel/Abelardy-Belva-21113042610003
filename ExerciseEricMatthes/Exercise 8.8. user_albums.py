def make_album(artist, title, songs=None):
    """Membuat dictionary yang mendeskripsikan sebuah album."""
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album


while True:
    print("\nMasukkan nama artis dan judul album.")
    print("(Ketik 'q' kapan saja untuk berhenti.)")
    artist = input("Artis: ")
    if artist == "q":
        break
    title = input("Judul album: ")
    if title == "q":
        break
    album = make_album(artist, title)
    print(album)