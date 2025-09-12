from rich.console import Console
console = Console()

def is_strong_password(password):
    return len(password) >= 8
def main():
    parol = input("Parol kiriting: ")

    if is_strong_password(parol):
        console.print("Kuchli parol", style="green")
    else: 
        console.print("Kuchsiz parol", style="red")

main()
