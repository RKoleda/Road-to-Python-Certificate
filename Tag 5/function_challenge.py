def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

def add(x, y):
    return x + y

def display_invoice(name, amount, due_date):
    print(f"Sehr geehrter Herr {name}")
    print(f"Ihre Rechnung in Hoehe von ${amount:.2f} ist faellig am {due_date}")
    
full_name = create_name("Markus", "Mueller")
betrag = add(100.25, 50.25)
display_invoice(full_name, betrag, "01.09.2025")
