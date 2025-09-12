from rich.console import Console
from rich.table import Table
console = Console()

def get_grade(score):
    grade = ""
    
    if 90<= score and score<=100:
        grade = "A"
    elif 80<=score and score<=89:
        grade = "B"
    elif 70<=score and score<=79:
        grade = "C"
    elif 60<=score and score<=69:
        grade = "D"
    elif 0<=score and score<=59:
        grade = "F"
    return grade

ball = int(input("Ball: "))
grade = get_grade(ball)

table = Table(title="Baholash natijasi")

table.add_column("Ball", justify="center", style="blue", no_wrap=True)
table.add_column("Baho", justify="center", style="magenta")

table.add_row(str(ball), grade)

console.print(table)
