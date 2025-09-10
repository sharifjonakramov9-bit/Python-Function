def is_palindrome(text):
    return text == text[:: -1]

text = input("So'z kiriting: ")
if is_palindrome(text):
    print("Bu so'z plindrom")
else:
    print("Bu so'z plindrom emas.")

