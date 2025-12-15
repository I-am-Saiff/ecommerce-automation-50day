#1. Define our product variables (The inputs)
item_name = "Wireless Headphones"
price = 49.99
quantity = 5
manufacturer_cost = 20.00

# 2. Calculate total revenue
revenue = price * quantity

# 3. Display the rsults (The output)
print("--- Daily Sales Report ---")
print("Item sold: " + item_name)
print(revenue)
# 4. Calculate profit
profit = revenue - (quantity * manufacturer_cost)
print(f'Your profit from selling {quantity} {item_name} is: ${profit:.2f}')

