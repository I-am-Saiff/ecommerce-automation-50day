order_id = "SHP-7832"
cst_name = "Alice Johnson"
order_message = (f" Your order {order_id} has been confirmed for customer {cst_name}.")
print(order_message)

from decimal import Decimal

price = Decimal("49.99")
tax = Decimal("0.07")
total_price = price + (price * tax)
print(f"The total price after tax is: ${total_price}")