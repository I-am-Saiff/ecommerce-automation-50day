def verify_amount(amount_str):
    # Converts string to int and checks safety limits
    val = int(amount_str)
    if val > 1000000:
        return "Fraud"
    if val == 0:
        return "Skip"
    return val