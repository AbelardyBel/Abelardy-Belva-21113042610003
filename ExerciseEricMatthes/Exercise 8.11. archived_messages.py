def show_messages(messages):
    """Menampilkan tiap pesan teks."""
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Mencetak tiap pesan dan memindahkannya ke sent_messages."""
    while messages:
        current = messages.pop()
        print(current)
        sent_messages.append(current)


pesan = ["Halo!", "Apa kabar?", "Sampai jumpa!"]
sent_messages = []
send_messages(pesan[:], sent_messages)
print("\nPesan asli:")
print(pesan)
print("\nPesan yang sudah terkirim:")
print(sent_messages)