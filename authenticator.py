from rules import validate_email, validate_password

data = [
    {"email": "saif@gmail.com", "password": 232423243},
    {"email": "saif#emailcom", "password": 1234567}
]

def authenticate_users():
    authenticated_users = []
    
    for user in data:
        try:
            email = user["email"]
            password = user["password"]
            
            email_is_valid = validate_email(email)
            password_is_strong = validate_password(password)
            
            if not email_is_valid:
                print(f"⏩ Skipping user: {email} (invalid email)")
                continue
            
            if not password_is_strong:
                print(f"🛑 THREAT: User {email} has weak password. STOPPING.")
                break
            
            authenticated_users.append(user)
            print(f"✓ User {email} authenticated successfully")
            
        except Exception as e:
            print(f"✗ Error processing user: {e}")
    
    return authenticated_users