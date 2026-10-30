sandwich_orders = ["pastrami", "tuna", "pastrami", "ayam", "pastrami", "keju"]
finished_sandwiches = []
print("Deli kehabisan pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Saya sudah membuat sandwich {sandwich} Anda.")
    finished_sandwiches.append(sandwich)
print("\nSemua sandwich sudah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(sandwich)