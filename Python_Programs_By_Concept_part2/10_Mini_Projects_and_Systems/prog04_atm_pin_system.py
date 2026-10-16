# Program: ATM PIN Simulation System
# Validates PIN with 3 attempts.
# Once granted, provides mini-banking options: Check Balance, Deposit, Withdraw.

CORRECT_PIN = "2026"
balance = 15000.0
attempts = 3
authenticated = False

print("=== WELCOME TO ANTIGRAVITY BANK ATM ===")

while attempts > 0:
    pin = input(f"Enter your 4-digit ATM PIN (Attempts left: {attempts}): ")
    if pin == CORRECT_PIN:
        print("\nPIN Verified Successfully! Access Granted.")
        authenticated = True
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect PIN! Please try again.")
        else:
            print("\nCard Blocked! You have exceeded 3 attempts. Contact customer support.")

if authenticated:
    while True:
        print("\n--- ATM OPERATIONS MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit / Remove Card")

        choice = input("Select option (1-4): ")

        if choice == "1":
            print(f"Current Account Balance: Rs. {balance:.2f}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: Rs. "))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited Rs. {amount:.2f}")
                print(f"New Balance: Rs. {balance:.2f}")
            else:
                print("Invalid deposit amount!")
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: Rs. "))
            if 0 < amount <= balance:
                balance -= amount
                print(f"Please collect your cash: Rs. {amount:.2f}")
                print(f"Remaining Balance: Rs. {balance:.2f}")
            else:
                print("Insufficient balance or invalid amount!")
        elif choice == "4":
            print("Thank you for using our ATM service. Please take your card.")
            break
        else:
            print("Invalid selection! Try again.")
