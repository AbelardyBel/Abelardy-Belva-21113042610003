sandwich_orders = ["tuna", "ayam", "keju", "daging"]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Saya sudah membuat sandwich {sandwich} Anda.")
    finished_sandwiches.append(sandwich)
print("\nSemua sandwich sudah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich)