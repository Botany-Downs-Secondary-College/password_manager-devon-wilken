import time
user_input = []
def add_to_list(x, y, z):
    add = [x, y, z]
    user_input.append(add)
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