from random import randint
from rich.console import Console
from rich.prompt import Prompt
prompt = Prompt()
console = Console()


def x():

    random_number = randint(1, 20)
    tries = 0
    
    while True:
        guess = int(prompt.ask("Tahmin: "))
        tries += 1

        if guess < random_number:
            console.print("Katta son", style="yellow")

        elif guess > random_number:
            console.print("Kichkik son", style="cyan")

        elif guess == random_number:
            console.print(f"{tries} ta urinishda topdingiz", style="red")
            break

x()

