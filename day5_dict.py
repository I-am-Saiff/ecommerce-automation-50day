from decimal import Decimal

# Defining a Dictionary
agent_settings = {
    'agent_name': 'FinanceBot',
    'role': 'Tax Calculator',
    'precision_level': 4,
    'is_active': True
}

# Accessing Data (Using the Key)
print(f'Current Agent: {agent_settings["agent_name"]}')
print(f'Role: {agent_settings["role"]}')

# Updating Data

agent_settings['is_active'] = False
print(f'Status Updated: Active = {agent_settings["is_active"]}')

# Adding new data
agent_settings['version'] = '1.0.2'

orders = [
    {"id": 101, "customer": "Zain", "total": Decimal("50.00")},
    {"id": 102, "customer": "Sarah", "total": Decimal("120.00")}
]

for order in orders:
    # We grab the value using the key ['customer']
    print(f"Processing order for {order['customer']}...")