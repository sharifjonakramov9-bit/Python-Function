def is_strong_password(password):
    return len(password) >= 8

parol = input("Parol kiriting: ")

if is_strong_password(parol):
    print("Kuchli parol")
else: 
    print("Kuchsiz parol")
