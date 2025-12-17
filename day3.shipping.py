from decimal import Decimal

# 1. Inputs (Simulation of  an order)
order_total = Decimal('30.00')

# Decision Logic
if order_total >= Decimal('100.00'):
    shipping_cost = Decimal('0.00')
    tier = 'VIP Free Shipping'
elif order_total >= Decimal('50.00'):
    shipping_cost = Decimal('8.00')
    tier = 'Standard Flat Rate'
else:
    shipping_cost = Decimal('15.00')
    tier = 'Economy Rate'

# Final Calculation
grand_total = order_total + shipping_cost

# Professional Output
print(f'--- Checkout Summary ---')
print(f'Order Subtotal: ${order_total:.2f}')
print(f'Shipping Cost ({tier}): ${shipping_cost:.2f}')
print(f'Total to Pay: ${grand_total:.2f}')
