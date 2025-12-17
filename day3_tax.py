from decimal import Decimal

# Calculating tax on US states  

tax_nyc = Decimal('0.08875')  # New York City tax rate
tax_ca = Decimal('0.0725')    # California tax rate
tax_rest_states = Decimal('0')  # Generic tax rate for other states

state = 'TX'  # Example state input
subtotal = Decimal('100.00')  # Example subtotal input

if state == 'NY':
    tax_rate = tax_nyc
elif state == 'CA':
    tax_rate = tax_ca
else:
    tax_rate = tax_rest_states

tax_amount = subtotal * tax_rate
grand_total = subtotal + tax_amount

print(f'Shipping to state: {state} costs ${tax_amount:.2f} in taxes.')