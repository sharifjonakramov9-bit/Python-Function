def calculate_bmi():
    weight = float(input("Vazn: "))
    height = float(input("Bo'y: "))
    bmi = weight / (height ** 2)
    return bmi

def bmi_status(bmi):
    if bmi<18.5:
        return "Vazn olish"
    elif 18.5 <= bmi and bmi < 25:
        return "Normal"
    elif 25 <= bmi and bmi < 30:
        return "Ortiqcha vazn"
    else:
        return "Semizlik"

bmi = calculate_bmi()
print("Test natijasiga ko'ra", round(bmi, 2))
print("Holat", bmi_status(bmi))

