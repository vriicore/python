# Program: Fruits Buying & Selling Profit / Loss Tracker
# Dictionary of fruits storing (buying_price, selling_price).
# Display fruits with profit, fruits with loss, and no profit no loss.

fruits = {
    "Apple": (100, 120),
    "Banana": (40, 35),
    "Orange": (60, 60),
    "Mango": (80, 110),
    "Grapes": (70, 65),
    "Guava": (50, 50)
}

profit_fruits = []
loss_fruits = []
no_profit_loss = []

for fruit, (buy, sell) in fruits.items():
    if sell > buy:
        profit_fruits.append(fruit)
    elif sell < buy:
        loss_fruits.append(fruit)
    else:
        no_profit_loss.append(fruit)

print("Fruit Price Records (Buying, Selling):", fruits)
print("\n1. Fruits sold at Profit (Selling > Buying) :", profit_fruits)
print("2. Fruits sold at Loss (Selling < Buying)   :", loss_fruits)
print("3. Fruits with No Profit No Loss            :", no_profit_loss)
