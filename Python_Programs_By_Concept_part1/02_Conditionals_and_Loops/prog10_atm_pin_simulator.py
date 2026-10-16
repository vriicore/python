# Program 1.22: ATM PIN Simulator
# Set a correct PIN (hardcoded). Give user 3 attempts.
# Use while loop with break. Display "Access Granted" or "Card Blocked" based on outcome.

CORRECT_PIN = "1234"
attempts = 3

while attempts > 0:
    entered_pin = input(f"Enter your 4-digit ATM PIN (Attempts left: {attempts}): ")
    if entered_pin == CORRECT_PIN:
        print("PIN verified successfully! Access Granted.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect PIN. Please try again.")
        else:
            print("You have exceeded 3 attempts! Card Blocked. Please contact bank.")
