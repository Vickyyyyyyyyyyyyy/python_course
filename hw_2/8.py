elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

elements.sort(key=lambda e: (e[1], e[2]))

print(elements)



