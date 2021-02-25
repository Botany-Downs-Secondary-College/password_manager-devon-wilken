def check_password(x):
    while True:
        check = len(x)
        if check >= 8:
            print("password meets requirements")
            break
        else:
            x = input("please provide a password that has 8 characters")

password = input("Password(must be at least 8 characters long:")
check_password(password)
print("thank you for using password manager")
