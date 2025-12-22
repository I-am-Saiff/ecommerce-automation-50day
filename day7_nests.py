from decimal import Decimal

raw_data = " !!_US_STOCK_PURCHASE_!! "

# Step 1: Clean the raw string

cleaned_data = raw_data.strip().replace("!!", "").replace("_", " ")
cleaned_data = cleaned_data.strip()

# Fetching only US and STOCK Parts

parts = cleaned_data.split()
fetched_parts = parts[0:2]
print(f"Fetched Parts: {fetched_parts}")  # Fetch US and STOCK

transaction = {"country": "US", "type": "STOCK"}
from decimal import Decimal

transaction = {"country": "US", "type": "STOCK"}

if transaction["country"] == "US":
    # These two checks should be independent or use elif
    if transaction["type"] == "STOCK":
        tax_rate = Decimal("0")
    elif transaction["type"] == "SERVICE":
        tax_rate = Decimal("0.10")
    else:
        tax_rate = Decimal("0.15") # Catch-all for other US types
else:
    tax_rate = Decimal("0.20") # UK/Global rate

print(f"Corrected Tax Rate: {tax_rate}")
