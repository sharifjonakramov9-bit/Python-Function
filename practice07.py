def x(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()
from getpass import getpass
def y(question, correct_answer):
    
    user_answer = input(question + " ")
    if x(user_answer, correct_answer):
        print("To'g'ri javob! ")
    else:
        print(f"No'to'g'ri! To'g'ri javob {correct_answer}")


y("O'zbekiston poytaxti qaysi shahar?", "Toshkent")
