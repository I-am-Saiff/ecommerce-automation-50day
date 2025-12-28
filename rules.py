def validate_email(email):
    """Returns True if valid, False if invalid"""
    if '@' not in email or "." not in email:
        return False
    return True

def validate_password(password):
    """Returns True if strong, False if weak"""
    if password < 8:
        return False
    return True
