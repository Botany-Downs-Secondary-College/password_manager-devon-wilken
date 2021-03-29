#Devon Wilken

#Password Manager 22/02/21
import time
accounts = {"DevonWilken": "DevonWilken1234"}
user_input = []
tries = 3

def add_account(account, accounts_password):
    accounts[account] = accounts_password
    print("account created")
def check_password(x):
    while True:
        check = len(x)
        if check >= 8:
            print("password meets requirements")
            break
        else:
            x = input("please provide a password that has 8 characters")
def add_to_list(x, y, z):
    add = [x, y, z]
    user_input.append(add)


name = input("Hello, what is your name?")
age = float(input("What is your age?"))
while True:
    if age < 13:
        print("you do not qualify to make an account")
        print(" Thank you {} for using pasword manager".format(name))
        raise SystemExit

    else:
        while True:
            try:
                print("1) Log in to account")
                print("2) Create an account")
                mode_1 = float(input("Enter numbers 1 or 2 to chose a mode:"))
            #create account
                if mode_1 == 2:
                    account = input("New account name:")
                    account_password = input("New account Password")
                    add_account(account, account_password)
                    break
            #log in to account
                elif mode_1 == 1:
                    while tries > 0:
                        account = input("What is your account username:")
                        account_password = input("What is your password?")
                        if accounts.get(account) == account_password:
                            print("pasword and username match")
                            break
                        else:
                            tries = tries - 1
                            print("incorrect pasword or account username {} tries left".format(tries))
                    break
                else:
                    print("please enter a valid niumber (1 or 2)")
            except ValueError:
                print("please enter a valid number(1 or 2)")

    while True:
        print("-----Menu-----")
        print("1) Save Password, username and app/website")
        print("2) Veiw Passwords, username and app/Website")
        print("3) Exit")
        try:
            option = float(input("Enter 1 2 or 3:"))
            if option == 1:
                website = input("Name of Website or app:")
                account_username = input("Account name: ")
                password = input("Account Password:")
                add_to_list(website, account_username, password)
            elif option == 2:
                print("| Website/app    | Username         | Password      |")
                for item in user_input:
                    print("|", item[0]," " * (13 - len(item[0])), "|", item[1]," " * (15 - len(item[1])), "|", item[2]," " * (12 - len(item[2])), "|")
                    time.sleep(2)
            elif option == 3:
                print("Thank you for using password manager")
                print("Goodbye")
                break
            else:
                print("Enter 1,2 or 3")
        except ValueError:
            print("please enter a valid number 1,2 or 3")