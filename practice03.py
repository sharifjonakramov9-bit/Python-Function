def is_even(x):  
    return x % 2 == 0

def print_even_message(x):
    if is_even(x):
        print("Berilgan son juft. ")
    else:
        print("berilgan son toq.")

num = int(input("Son kiriting: "))
print_even_message(num)

