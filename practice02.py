from datetime import date 

def x(tugilgan_yil):
    y = date.today()

    age = y.year - tugilgan_yil
    return age


name = input('Name: ') 
yil = int(input("Tug'ilgan yiliz: "))

age = x(yil)
print(f"{name}, sizning yoshiz: {age} ")

if age >= 18:
    print("Siz balog'atga yetdingiz.")
else:
    print("Siz balog'atga yetmadingiz.")
