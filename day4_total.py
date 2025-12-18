from decimal import Decimal

# 1. Our List of Orders
orders = [Decimal("45.00"), Decimal("120.50"), Decimal("12.00"), Decimal("300.00")]

# 2. INITIALIZE the Accumulator (The empty cash drawer)
# This MUST stay outside the loop
grand_total = Decimal("0.00")

print("--- Processing Daily Sales ---")

# 3. The Loop
for amount in orders:
    # Add the current order to the running total
    grand_total += amount
    print(f"Added ${amount} to the register.")

# 4. Final Output (Outside the loop!)
print("------------------------------")
print(f"TOTAL REVENUE FOR TODAY: ${grand_total}")