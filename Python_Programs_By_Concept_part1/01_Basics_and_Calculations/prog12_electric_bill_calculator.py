# Program 1.12: Electric Bill Calculator
# Take previous meter reading and current meter reading as input.
# Units consumed = current - previous.
# Bill = units * 5.50 + fixed_charge(100). Display units consumed and total bill.

prev = float(input("Enter previous meter reading: "))
curr = float(input("Enter current meter reading: "))

if curr < prev:
    print("Invalid reading! Current reading cannot be less than previous.")
else:
    units = curr - prev
    fixed_charge = 100
    bill = (units * 5.50) + fixed_charge

    print("Units Consumed:", units)
    print("Fixed Charge  : Rs.", fixed_charge)
    print("Total Bill    : Rs.", bill)
