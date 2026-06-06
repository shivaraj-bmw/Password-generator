import random

password = ""

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#&!$%"

length = int(input("Enter password length: "))

if length <= 0:
    print("Enter positive number")

else:
    for i in range(length):
        password += random.choice(chars)

    print("Your password:", password)

    if length < 8:
        print("Password Strength: Weak")

    elif length < 12:
        print("Password Strength: Medium")

    else:
        print("Password Strength: Strong")
