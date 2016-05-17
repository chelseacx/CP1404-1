from guitar import Guitar

guitars = []

print("My guitars!")
name = str(input("Name: "))
year = int(input("Year: "))
cost = float(input("Cost: $"))

guitars.append(Guitar(name, year, cost))
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("These are my guitars:")

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
    else:
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}".format(i + 1, guitar.name, guitar.year, guitar.cost))
