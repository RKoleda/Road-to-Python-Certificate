def happy_birthday(name, age):
    print(f"Happy Birthday {name}")
    print(f"You are {age} old")
    
    
happy_birthday("Markus", 86)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due on {due_date}")
    
display_invoice("Frank Martin", 89.56, "01.08.2025")

def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z  

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(5, 6))
print(multiply(4, 6))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("dieter", "heiner")

print(full_name)