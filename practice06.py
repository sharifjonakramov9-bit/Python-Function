from rich.console import Console
from rich.prompt import Prompt
prompt = Prompt()
console = Console()


def is_valid_phone_number(phone):
    result = phone.isdigit() and len(phone) == 9

    return result

tries = 0
def main():
    tries = 0
    while True:
        phone = Prompt.ask("Phone: ")
        tries += 1
        if is_valid_phone_number(phone):
            console.print(f"Phone number to'g'ri: {tries}", style="green")
            break
        else:
            console.print("Phone number noto'g'ri", style="red")
            continue

main()
