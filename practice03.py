from rich.console import Console
console = Console()

def is_even(x):  
    return x % 2 == 0

def print_even_message(x):
    if is_even(x):
        console.print("Berilgan son juft. ", style="cyan")
    else:
        console.print("berilgan son toq.", style="magenta")

num = int(input("Son kiriting: "))
print_even_message(num)

