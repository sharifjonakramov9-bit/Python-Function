def is_valid_phone_number(phone):
    result = phone.isdigit() and len(phone) == 9

    return result

tries = 0
while True:
    phone = input("Phone: ")
    tries += 1
    if is_valid_phone_number(phone):
        print(f"Phone number to'g'ri: {tries}")
        break
    else:
        print("Phone number noto'g'ri")
        continue

