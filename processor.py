from vault import verify_amount

data = ["500", "0", "1500000", "200"]

for item in data:
    try:
        result = verify_amount(item)
        
        if result == "Skip":
            print(f"Skipping zero amount")
            continue
        if result == "Fraud":
            print("Alert! Fraud detected. Loop terminated.")
            break
            
        print(f"Adding {result} to secure ledger.")
    except ValueError:
        print("Corrupt data skipped.")