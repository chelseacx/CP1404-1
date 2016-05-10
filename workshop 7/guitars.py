from guitars_class import Guitar
print("My guitars!")

list=[]

name=str(input("Name: "))
year=int(input("Year: "))
cost=float(input("Cost: "))

list.append(Guitar(name, year, cost))
list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("… snip …  ")
print("These are my guitars: ")

for i, guitar in enumerate(list):
    vintage_string = "(vintage)"
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))