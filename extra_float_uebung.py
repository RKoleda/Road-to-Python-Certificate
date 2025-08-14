zahl1 = float(input("Bitte geben Sie die Erste Zahl ein: "))
zahl2 = float(input("Bitte geben Sie die zweite Zahl ein: "))
zahl3 = float(input("Bitte geben Sie die dritte Zahl ein: "))

if zahl1 > zahl2 and zahl1 > zahl3:
    print("Die erste Zahl ist die Groesste")
elif zahl2 > zahl1 and zahl2 > zahl3:
    print("Die zweite Zahl ist die Groesste")
elif zahl3 > zahl1 and zahl3 > zahl2:
    print("Die dritte Zahl ist die Groesste")
elif zahl1 == zahl2 or zahl1 == zahl3 or zahl2 == zahl3:
    print("Es gibt mehrere grosse Zahlen")
    
    