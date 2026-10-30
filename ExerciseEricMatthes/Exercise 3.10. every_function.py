gunung = ["Bromo", "Rinjani", "Semeru", "Merbabu", "Prau"]
print(gunung[0])
gunung.append("Slamet")
gunung.insert(0, "Kerinci")
del gunung[1]
gunung.pop()
gunung.remove("Merbabu")
print(sorted(gunung))
gunung.reverse()
gunung.sort()
gunung.sort(reverse=True)
print(len(gunung))
print(gunung)