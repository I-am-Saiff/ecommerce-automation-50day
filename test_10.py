internal_ledger_data = """id,amount,date,description
TXN001,500.00,2025-01-15,Withdraw,
TXN002,500.00,2025-01-15,DEPOSIT,
TXN003,500.00,2025-01-16,PAYMENT Withdraw,
TXN004,500.00,2025-01-19,REFUND
"""

with open("internal_ledger.csv", "w") as  file:
    file.write(internal_ledger_data)

bank_data = """amount,date,description
500.00,2025-01-15,Withdraw,
500.00,2025-01-15,DEPOSIT,
400.00,2025-01-16,PAYMENT Withdraw,
-500.00,2025-01-21,REFUND
"""

with open("bank_data.csv", "w") as file:
    file.write(bank_data)

# read internal ledger
with open("internal_ledger.csv", "r") as file:
    internal_lines = file.readlines()
# read bank ledger
with open("bank_data.csv", "r") as file:
    bank_lines = file.readlines()
print(f'Read {len(internal_lines)} internal transactions')
print(f'Read {len(bank_lines)} bank transactions')

# parsing internal ledger
internal_transactions = []
for line in internal_lines[1:]: #skips header and continues to perform action
    line = line.strip()
    parts = line.split(",")
    internal_transactions.append({
        "id": parts[0],
        "amount": float(parts[1]),
        "date": parts[2],
        "description": parts[3]
    })

# parsing bank feed
bank_transactions = []
for line in bank_lines[1:]:
    line = line.strip()
    parts = line.split(",")
    bank_transactions.append({
        "amount": float(parts[0]),
        "date": parts[1],
        "description": parts[2]
    })

    print("\n" + "="*70)
    print("parsed internal ledger:")
    print("="*70)
    for txn in internal_transactions:
        print(txn)

    
    print("\n" + "="*70)
    print("parsed bank ledger:")
    print("="*70)
    for txn in bank_transactions:
        print(txn)

# initialize tracking lists
matched = []
unmatched_internal = []
unmatched_bank = []
# track which bank transactions have been matched
matched_bank_indices = set()
#outer loop: each internal transaction
for i, internal_txn in enumerate(internal_transactions):
    found_match = False
    #inner loop: each bank transaction
    for j, bank_txn in enumerate(bank_transactions):
        if j in matched_bank_indices:
            continue
        #checking if amounts exactly match
        if internal_txn["amount"] != bank_txn["amount"]:
            continue
        if "withdraw" not in internal_txn["description"].lower() and "withdraw" not in bank_txn["description"].lower():
                        if "deposit" not in internal_txn["description"].lower() and "deposit" not in bank_txn["description"].lower():
                             continue
        # if we reach here, we found a match
        matched.append({"internal": internal_txn, "bank": bank_txn})
        matched_bank_indices.add(j)
        found_match = True
        break
    #if no match found, add to unmatched_internal
    if not found_match:
         unmatched_internal.append(internal_txn)
    #find bank transactions that were never matched
for j, bank_txn in enumerate(bank_transactions):
     if j not in matched_bank_indices:
          unmatched_bank.append(bank_txn)

print("\n" + "="*70)
print("RECONCILIATION RESULTS:")
print("="*70)
print(f"\n✅ MATCHED: {len(matched)}")
for m in matched:
    print(f"   {m['internal']['id']}: ${m['internal']['amount']}")

print(f"\n⚠️  UNMATCHED IN INTERNAL: {len(unmatched_internal)}")
for t in unmatched_internal:
    print(f"   {t['id']}: ${t['amount']}")

print(f"\n⚠️  UNMATCHED IN BANK: {len(unmatched_bank)}")
for t in unmatched_bank:
    print(f"   ${t['amount']}: {t['description']}")
                        
