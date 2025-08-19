def summe(*zahlen):
    ergebnis = 0
    for z in zahlen:
        ergebnis += z
    return ergebnis

print(summe(54, 69))

def produkt(*zahlen):
    ergebnis = 1
    for z in zahlen:
        ergebnis *= z
    return ergebnis
    
print(produkt(8,56))

def verdoppeln(x):
    return x * 2

print(verdoppeln(5))

def maximum(x, y):
    return max(x, y)
print(maximum(8, 20))

def greatest(x ,y):
    if x < y:
        return y
    else:
        return x
print(greatest(89, 98))

def liste_summe(liste):
    ergebnis = 0
    for z in liste:
        ergebnis = ergebnis + z
    return ergebnis

print(liste_summe([1, 2, 3, 4, 5, 6, 7,]))