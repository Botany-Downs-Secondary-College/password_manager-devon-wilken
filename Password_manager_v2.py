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
