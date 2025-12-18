from decimal import Decimal

# Inventory Warning System

inventory = [Decimal("15"), Decimal("2"), Decimal("45"), Decimal("4"), Decimal("10")]

print("--- Inventory Stock Report ---")

for stock in inventory:
    if stock < Decimal("5"):
        print(f"WARNING: Low stock level - only {stock} items left!")
    else:
        print(f"Stock level is sufficient: {stock} items available.")