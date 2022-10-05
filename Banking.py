from accounts import Account


if __name__ == '__main__':
    while True:
        option = input(
            "Enter 1.Create Account 2.Closing Account 3. Pin Change 4.Deposit")
        if option == '1':
            name = input("Enter Name: ")
            acc = Account(name=name)
            acc.create_account()
