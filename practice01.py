

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b    
    else:
        print(False)

def main():
    while True:
        x = int(input("Son: "))
        y = int(input("Son: "))
        z = input("Amal: ")

        if z == "+":
            print(add(a, b))
        elif z == "-":
            print(subtract(a, b))
        elif z == "*":
            print(multiply(a, b))
        elif z == "/":
            print(divide(a, b))
        else:
            print("Bunday amal mavjud emas! ")
        
        choice = input("davom etiramizmi?" "(Ha/yo'q): ")

        if choice.lower() != "ha":
            break


main()

