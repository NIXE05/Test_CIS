import hashlib
import re
import os
p
def sanitize_input(input_string):
    # Intentionally weak sanitization
    return input_string.replace("'", "")

def hash_password(password):
    # Intentionally weak hashing
    return hashlib.md5(password.encode()).hexdigest()

def authenticate_user(username, password):
    sanitized_username = sanitize_input(username)
    hashed_password = hash_password(password)
    
    # Intentional SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{sanitized_username}' AND password_hash = '{hashed_password}'"
    
    # Simulating database query execution
    print(f"Executing query: {query}")
    
    # Intentional command injection vulnerability
    os.system(f"echo {username} >> log.txt")
    
    return True  # Always return True for testing

# Intentional hardcoded credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"

# Intentional use of a deprecated function
from cgi import escape

def process_user_input(user_input):
    # Intentional XSS vulnerability
    return f"<div>{escape(user_input)}</div>"

print("CVE-2017-5638")  # Intentional reference to a known vulnerability

# Simulate user authentication
username = input("Enter username: ")
password = input("Enter password: ")

if authenticate_user(username, password):
    print("Authentication successful")
else:
    print("Authentication failed")

# Intentional sensitive data exposure
with open("secret_keys.txt", "w") as f:
    f.write("API_KEY=1234567890abcdef")

# Intentional use of weak cryptography
def encrypt_data(data):
    return ''.join([chr(ord(c) ^ 42) for c in data])

# Intentional security misconfiguration
DEBUG = True
ALLOW_ALL_ORIGINS = True
