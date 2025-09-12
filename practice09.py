from rich.console import Console
console = Console()


def show_menu():
    console.print("---------Menu--------", style="yellow")
    console.print("1.Balansni ko'rish", style="yellow")
    console.print("2.Pul kiritish", style="yellow")
    console.print("3.Pul yechish", style="yellow")
    console.print("0.Chiqish", style="yellow")

def deposit(balance, amount):
    if amount > 0:
        balance += amount
    return balance


def withdraw(balance, amount):
    if amount<=balance:
        balance -= amount

    return balance 
    
def check_balance(balance):
    console.print(f"Sizning balansingiz: {balance}", style="cyan")

def main():
    balance = 100.00

    while True:
        show_menu()

        op = input("> ")

        if op == "1":
            check_balance(balance)
        elif op == "2":
            amount = float(input("Amount: "))
            balance = deposit(balance, amount)
        elif op == "3":
            amount = float(input("Amount: "))
            balance = withdraw(balance, amount)
        elif op == "0":
            break
        else:
            console.print("Bunday menu yo'q", style="red")

main()

         