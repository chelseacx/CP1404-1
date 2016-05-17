from programminglanguage import Methods

ruby = Methods("Ruby", "Dynamic", True, 1995)
print(ruby)
python = Methods("Python", "Dynamic", True, 1991)
print(python)
vb = Methods("Visual Basic", "Static", False, 1991)
print(vb)

List=[ruby,python,vb]
print("The dynamically typed languages are:")
for each in List:
    if each.is_dynamic():
        print(each.name)
