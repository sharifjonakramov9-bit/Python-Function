from rich.console import Console
from rich.prompt import Prompt
prompt = Prompt()
console = Console()

def x(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

from getpass import getpass

def y(question, correct_answer):
    tries = 0
    while True:
        user_answer = prompt.ask(question + " ")
        tries += 1
        if x(user_answer, correct_answer):
            console.print(f"To'g'ri javob! Urinishlar soni {tries} ", style="green")
            break
        else:
            console.print(f"No'to'g'ri! To'g'ri javob {correct_answer}", style="red")
            continue


y("O'zbekiston poytaxti qaysi shahar?", "Toshkent")
