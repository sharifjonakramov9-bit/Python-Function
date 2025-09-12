from rich.console import Console
from rich.prompt import Prompt
console = Console()
prompt = Prompt()

def c_to_f(celsius):
    F = 9 / 5 * celsius +32
    return F

def f_to_c(fahrenheit):
    C = 5 / 9 * (fahrenheit - 32)
    return C

def main():
    while True:
        console.print("""
----------MENU------------
 1 - Selsiydan Farangetga    
 2 - Farangetdan Selsiyga   
 3 - Dasturni yakunlash

""", style="yellow")
        check = prompt.ask(" ")
        if check == "1":
            celsius = float(prompt.ask("Selsiyning qiymatini kiriting: "))
            farangeyt = c_to_f(celsius)
            console.print (f"{celsius}==> {farangeyt} (Farangeyt)ga teng ", style="blue")

        elif check == "2":
            fahrenheit = float(prompt.ask("Farangeytning qiymatini kiriting: "))
            celsius = f_to_c(fahrenheit)
            console.print (f"{fahrenheit}==> {celsius} (Selsiy)ga teng ", style="blue")

        elif check == "3":
            console.print("Dastur tugadi! ", style="cyan")
            break
        
        else:
            console.print("Bunday menu mavjud emas!", style="red")
            
main()
