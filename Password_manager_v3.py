accounts = ["DevonWilken"]
accounts_password = ["Devon123"]
tries = 3
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
while True:
    try:
        print("1) Log in to account")
        print("2) Create an account")
        mode_1 = float(input("Enter numbers 1 or 2 to chose a mode:"))
        if mode_1 == 2:
            account = input("New account name:")
            account_password = input("New account Password")
            account_1 = Account(account, account_password)
            confirm_password(confirm_password)
            add_account(account, accounts_password)
            break
        elif mode_1 == 1:
            while tries > 0:
                account = input("What is your account username:")
                account_pasword = input("What is your password?")
                if account in accounts and account_pasword in accounts_password:
                    print("Welcome {}".format(account))
                    break
                else:
                    tries = tries - 1
                    print("incorrect pasword or account username {} tries left")
            break
        else:
            print("please enter a valid niumber (1 or 2)")
    except ValueError:
        print("please enter a valid number(1 or 2)")
print("Thank you for using Password Manager ")