from rich.console import Console
console = Console()

def calculate_tax(salary) :  
    if salary > 5_000_000: 
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary):
    x = calculate_tax(salary)
    return salary - x

y = int(input("Maoshingizni kiriting: "))

a = calculate_tax(y)
b = calculate_net_salary(y)

console.print("Sizning maoshingizdan olinadigan mablag':  ", a, "so'm.", style="blue")
console.print("Sof maosh: ", b, "so'm", style="cyan")
