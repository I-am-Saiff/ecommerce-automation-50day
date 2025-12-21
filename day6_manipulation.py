from decimal import Decimal

raw_ledger_entry = "  !!_2025_001//PAYMENT//RECONCILED//$5,000.50_!!  "

# Step 1: Clean the raw string

cleaned_ledger = raw_ledger_entry.strip().replace("!!", "").replace("$", "").replace(",", "").replace("_", " ").replace("//", " ")

cleaned_ledger = cleaned_ledger.strip()

print(f"Cleaned Ledger Entry: '{cleaned_ledger}'")