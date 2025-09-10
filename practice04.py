#Foydalanuvchi ball kiritadi → `A`, `B`, `C`, `F` baho qaytadi.
#* **Funksiya**:

# * `get_grade(score)`
#* **Qo‘llaniladigan narsa**: `if-elif-else`, `str`, `int`
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
print(grade)
