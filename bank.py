account = {
    "name" : "Faith",
    "balance" : 50000,
    "account_number" : "62378901765"
}

def account_menu():
    choice = 1
    while choice != 5:
        print(f"Hello {account['name']} welcome to account menu")
        print("Press 1 to check your balance")
        print("press 2 to deposit")
        print("press 3 to withdraw")
        print("press 4 to speak with a customer care representative")
        print("press 5 to exit this menu")
        choice = int(input("Choose an option: "))
        if choice == 1:
            print(f"Your balance is ₦{account['balance']}")
        elif choice == 2:
            deposit_amount = int(input("How much would you like to deposit? "))
            if deposit_amount > 0:
                account['balance'] += deposit_amount
                print(f"Your new balance is {account['balance']}")
            else:
                print("INVALID DEPOSIT AMOUNT")
        elif choice == 3:
            withdraw_amount = int(input("How much would you like to withdraw? "))
            if withdraw_amount > 0 and withdraw_amount <= account['balance']:
                account['balance'] -= withdraw_amount
                print(f"Your new balance is ₦ {account['balance']}")
            else:
                print("INSUFFICIENT FUNDS")
        elif choice == 4:
            print("Welcome to account_menu customer care service")
            print("press 1 to report a problem")
            print("press 2 to speak whith an agent")
            print("press 3 to return back to menu")
            choice2 = 1
            while choice2 != 3:
                choice2 = int(input("choose an option: "))
                if choice2 == 1:
                    print("Please describe your problem.")
                elif choice2 == 2:
                    print("Connecting you to a customer care agent.....")
                elif choice2 ==3:
                    print("Back to menu")
                else:
                    print("Invalid option")
        elif choice == 5:
            print("Thank you for using account_menu. Goodbye")
        else:
            print("INVALID OPTION. Please choose from 1-5")
account_menu()

