from bank.savings_account import SavingsAccount
from utils.menu import show_menu



from bank.exceptions import InsufficientFundsError
def main():
    name = input("Enter the name")
    account = SavingsAccount(name,1000)

    while True:
        show_menu()
        choice = input("Enter the number")

        try:
            if choice == "1":
                amt = int(input("Enter the amount"))
                account.deposit(amt)
            elif choice == "2":
                amt = int(input("Enter amount:  "))
                account.withdraw(amt)

            elif choice =="3":
                print(f"Your Available balance is {account.get_balance()}")
            elif choice =="4":
                print("Thank you for banking with us!!")
            else:
                print("Invalid choice")
        except InsufficientFundsError as e:
            print("error",e)
        except ValueError:
            print("Invalid amount")

if __name__ == "__main__":
    main()



        