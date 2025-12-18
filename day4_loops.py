from decimal import Decimal

#1. Our "Containers" of orders (The List)
orders = [Decimal("45.00"), Decimal("120.50"), Decimal("12.00"), Decimal("300.00")]
tax_rate = Decimal("0.08875") # NY Tax

print("--- Bulk Tax Report ---")

#2. The Assembly Line (The Loop)
for amount in orders:
    tax = amount * tax_rate
    total = amount + tax

    # We use the f-string inside the loop to print for Each order


    print(f'order: ${amount:>7} | Tax: ${tax:>5.2f} | Total: ${total:>7.2f}')

print("---------------------------")
print("Process Complete!")


if total > Decimal("100.00"):
    print("FLAG: HIGH VALUE ORDER")
else:
    print("Standard Order")