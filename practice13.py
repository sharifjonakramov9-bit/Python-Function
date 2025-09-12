from rich.console import Console
console = Console()

def is_palindrome(text):
    return text == text[:: -1]
def main():
    text = input("So'z kiriting: ")
    if is_palindrome(text):
        console.print("Bu so'z plindrom", style="green")
    else:
        console.print("Bu so'z plindrom emas.", style="red")

main()

