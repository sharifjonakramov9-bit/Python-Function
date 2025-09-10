def show_menu():
    print("---------Menu--------")
    print("1.Balansni ko'rish")
    print("2.Pul kiritish")
    print("3.Pul yechish")
    print("0.Chiqish")

def deposit(balance, amount):
    if amount > 0:
        balance += amount
    return balance


def withdraw(balance, amount):
    if amount<=balance:
        balance -= amount

    return balance 
    
def check_balance(balance):
    print(f"Sizning balansingiz: {balance}")

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
            print("Bunday menu yo'q")

main()

         