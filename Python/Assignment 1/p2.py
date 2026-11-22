# 2.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity = int(input("Enter the quantity: "))
unitCost = 100
totalCost = quantity * unitCost
if totalCost > 1000:
    dis = totalCost * 0.10
    totalCost = totalCost-dis 
    print("total cost after 10% dis", {totalCost})
else:
    print(f"Total cost: {totalCost}")

