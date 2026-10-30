pizza = ["pepperoni", "margherita", "jamur"]
pizza_teman = pizza[:]
pizza.append("keju")
pizza_teman.append("barbekyu")
print("Pizza favorit saya adalah:")
for p in pizza:
    print(p)
print("\nPizza favorit teman saya adalah:")
for p in pizza_teman:
    print(p)