from rich.console import Console
from rich.table import Table
console = Console()
tablse = Table()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b    
    else:
        print(False)

def main():
    while True:
        x = int(input("Son: "))
        y = int(input("Son: "))
        z = input("Amal: ")

        if z == "+":
            result = add(x, y)
        elif z == "-":
            result = subtract(x, y)
        elif z == "*":
            result = multiply(x, y)
        elif z == "/":
            result = divide(x, y)
        else:
            console.print("Bunday amal mavjud emas! ", style="red")
        
        console.print(f"Natija: {result}", style="green")
        choice = input("davom etiramizmi?" "(Ha/yo'q): ").lower()

        if choice.lower() != "ha" and choice.lower() != "":
            console.print("Dastur tugadi hayr!", style="yellow")
            break



main()

