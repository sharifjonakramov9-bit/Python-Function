from datetime import date 
from rich.console import Console
console = Console()

def x(tugilgan_yil):
    y = date.today()

    age = y.year - tugilgan_yil
    return age


def main(name, yil):
    age = x(yil)
    console.print(f"{name}, sizning yoshiz: {age} ", style="blue")

    if age >= 18:
        console.print("Siz balog'atga yetdingiz.",style="green")
    else:
        console.print("Siz balog'atga yetmadingiz.", style="red")

name = input('Name: ') 
yil = int(input("Tug'ilgan yiliz: "))
main(name, yil)
