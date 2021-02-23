#Devon Wilken
#Password Manager 22/02/21
accounts = ["DevonWilken"]
accounts_password = ["Devon123"]
class Account:
    def __init__(self, account, account_password):
        self.account = account
        self.account_password = account_password
def add_account(account, accounts_password):
    accounts.append(account)
    accounts_password.append(account_password)
    print("account created")
def confirm_password(confirm_password):
    confirm_password = input("Confirm Password:")
    if confirm_password == account_password:
        print("Pasword confirmed")
def check_password(x):
    while True:
        len(x)
        if x >= 8:
            print("password meets requirements")
            break
        else:
            x = input("please provide a password that has 8 characters")




name = input("Hello, what is your name?")
age = float(input("What is your age?"))
if age < 13:
    print("you do not qualify to make an account")
    print(" Thank you {} for using pasword manager".format(name))

else:
    while True:
        print("1) Log in to account")
        print("2) Create an account")
        mode_1 = float(input("Enter numbers 1 or 2 to chose a mode:"))
        if mode_1 == 2:
            account = input("New account name:")
            account_password = input("New account Password")
            account_1=Account(account,account_password)
            confirm_password(confirm_password)
            add_account(account, accounts_password)
            break
        elif mode_1 == 1:
            account = input("What is your account username:")
            account_pasword = ("What is your password?")
            break
        else:
            print("please enter a valid niumber (1 or 2)")
while True:







