fruechte = ("Apfel", "Banane", "Kirsche")
print("Vorher:", fruechte)

liste = list(fruechte)

liste.append("Mango")
liste[1] = "Erdbeere"

fruechte = tuple(liste)

print("Nacher:", fruechte)