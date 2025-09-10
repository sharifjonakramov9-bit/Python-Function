def calculate_tax(salary) : # Shartlarda nimadurlar berilib tashlagan uncha tushunmay qoldim
    if salary > 5_000_000: # keyin youtube dan video keyin chatGPT dan ozgina tushuncha olib ishlayapman
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary):
    x = calculate_tax(salary)
    return salary - x

y = int(input("Maoshingizni kiriting: "))

a = calculate_tax(y)
b = calculate_net_salary(y)

print("Sizning maoshingiz: ", a, "so'm.")
print("Sof maosh: ", b, "so'm")
