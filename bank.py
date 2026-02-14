
import os

class BankAccount:
    def __init__(self, acc_no=None, name=None, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Deposited successfully.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def display(self):
        print("\n--------Bank Account details--------")
        print("Account Holder name:", self.name)
        print("Account Number:", self.acc_no)
        print("Account Balance:", self.balance)
        print("-----------------------------------\n")


class BankSystem:
    FILE_NAME = "data.txt"

    def create_account(self):
        acc_no = input("Enter account number: ").strip()
        name = input("Enter account holder name: ").strip()
        balance = float(input("Enter initial balance: "))

        with open(self.FILE_NAME, "a") as file:
            file.write(f"{acc_no},{name},{balance}\n")

        print("Account created successfully.")

    def find_account(self, acc_no):
        acc_no = acc_no.strip()
        print(f"Searching for account number: {acc_no}")

        if not os.path.exists(self.FILE_NAME):
            return None

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                if not line.strip():
                    continue

                print("Checking line:", line.strip())
                data = line.strip().split(",")

                if data[0] == acc_no:
                    return BankAccount(data[0], data[1], float(data[2]))

        return None

    def update_account(self, account):
        with open(self.FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(self.FILE_NAME, "w") as file:
            for line in lines:
                if not line.strip():
                    continue

                data = line.strip().split(",")

                if data[0] == account.acc_no:
                    file.write(f"{account.acc_no},{account.name},{account.balance}\n")
                else:
                    file.write(line)

    def deposit_money(self):
        acc_no = input("Enter account number: ").strip()
        account = self.find_account(acc_no)

        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            self.update_account(account)
        else:
            print("Account not found.")

    def withdraw_money(self):
        acc_no = input("Enter account number: ").strip()
        account = self.find_account(acc_no)

        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
            self.update_account(account)
        else:
            print("Account not found.")

    def check_balance(self):
        acc_no = input("Enter account number: ").strip()
        account = self.find_account(acc_no)

        if account:
            account.check_balance()
        else:
            print("Account not found.")


def main():
    bank = BankSystem()

    while True:
        print("\n====== Banking System ======")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            bank.create_account()
        elif choice == "2":
            bank.deposit_money()
        elif choice == "3":
            bank.withdraw_money()
        elif choice == "4":
            bank.check_balance()
        elif choice == "5":
            print("Thank you. Visit again.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()