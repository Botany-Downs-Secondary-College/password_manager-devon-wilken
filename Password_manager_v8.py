#Devon Wilken

#Password Manager 22/02/21
import time
import re
tries = 3
# checks if the password is complex enough (meet requirements)
def check_password(password):
    while True:
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
        else:
            print("Your password is acceptable")
            break
    return(password)


#main routine
name = input("Hello, what is your name?")
while True:
    try:
        age = float(input("What is your age?"))
        if age < 13:
            print("you do not qualify to make an account")
            print(" Thank you {} for using pasword manager".format(name))
        elif age <= 122:
          print("age meets requirements")
          break
        else:
            print("please enter a valid age")
    except ValueError:
        print("please input valid age")
print("thankyou for using Password Manager ")

while True:
    try:
        print("1) Log in to account")
        print("2) Create an account")
        mode_1 = float(input("Enter numbers 1 or 2 to chose a mode \n>"))
    #create account
        if mode_1 == 2:
            account = input("New account name \n>")
            password = input("Enter a password \n> ")
            account_password = check_password(password)
        #write to file
            with open("secure_file.txt", 'a') as file:
                file.write("{} {}".format(account, account_password ))
                file.write("\n")
                break

    #log in to account
        elif mode_1 == 1:
            while True:
                account = input("What is your account username \n>")
                account_password = input("What is your password \n>")
                d = {}
                #read file and make it a list
                with open('secure_file.txt') as f:
                    d = dict(x.rstrip().split(None, 1) for x in f)
                if d.get(account) == account_password:
                    print("pasword and username match")
                    break
                else:
                    if tries == 1:
                        print("You have reached maximum tries, Program will shut down")
                        raise SystemExit
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
            website = input("Name of Website or app \n>")
            account_username = input("Account name \n>")
            password = input("Account Password \n>")
            with open("{}_passwords.txt".format(account), 'a') as file:
                file.write("{} {} {}".format(website, account_username, password))
                file.write("")
                
        elif option == 2:
            a_file = open("{}_passwords.txt".format(account), "r")
            list_of_lists = []
            for line in a_file:
                line_list = line.split()
                list_of_lists.append(line_list)
            a_file.close()
            print("| Website/app    | Username         | Password      |")
            for item in list_of_lists:
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
        