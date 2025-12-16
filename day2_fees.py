from decimal import Decimal

#Inputs
sale_price = Decimal("25.00")
stripe_percent = Decimal("0.029")
stripe_flat_fee = Decimal("0.30")

#Logic 
fee_amount = (sale_price * stripe_percent) + stripe_flat_fee
payout = sale_price - fee_amount

#Output
print(f'Sale Price: ${sale_price}')
print(f'Stripe Takes: ${fee_amount:.2f}')
print(f'Actual Payout: ${payout:.2f}')
