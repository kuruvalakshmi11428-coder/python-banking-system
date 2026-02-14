
print("Welcome to ATM!")

correct_bin = "1234"
balance = 2000
attempts = 2
while attempts >= 0:
    pin = input("Enter your PIN:")
    if pin == correct_bin:
        print("PIN accepted!")
        while True:
            print("Choose an option:") 
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                print(f"💰your balance is:  ${balance}")
            elif choice == '2':
                amount = int(input("Enter amount to deposit:"))
                balance += amount
                print(f"💰${amount} deposited. New balance is: ${balance}")
            elif choice == '3':
                amount = int(input("Enter amount to withdraw:"))
                if amount > balance:
                    print("Insufficient funds!")
                else:
                   balance -= amount
                   print(f"💰${amount} withdrawn. New balance is: ${balance}")
            elif choice == '4':
                print("👋Thank you for visiting the ATM!")
                exit()
            else:
                print("Invalid option. Please try again.")
      
else:
    attempts -= 1
    if attempts < 0:
        print("No attempts left. Your account is locked.")
    else:
        print(f"Incorrect PIN. You have {attempts + 1} attempts left.")
        print("Card blocked.too many attempts.")
   