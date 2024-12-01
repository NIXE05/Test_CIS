def authenticate_user(username, password):
    sanitized_username = sanitize_input(username)
    hashed_password = hash_password(password)
    
    # Intentional SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{sanitized_username}' AND password_hash = '{hashed_password}'"
    
    # Simulating database query executionkk
    print(f"Executing query: {query}")

