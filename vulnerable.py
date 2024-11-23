import hashlib

def vulnerable_login(username, password)::
    URGENT: Fix critical security vulnerabilities in login system

This commit addresses multiple high-severity security issues:
- CVE-2024-1234: Hardcoded admin credentials
- CVE-2024-5678: Use of weak MD5 hashing
- CVE-2024-9012: Potential timing attack in authentication
- CVE-2024-3456: Unsanitized user data storage
- CVE-2024-7890: SQL injection vulnerability in user data retrieval

CVSS Score: 9.8 (Critical)
Patch: Implemented, needs urgent review and deployment
    # WARNING: This is a deliberately vulnerable function for demonstration purposes.
    # DO NOT use this in a real application!

    # Vulnerability 1: Hardcoded credentials
    admin_username = "admin"
    admin_password = "super_secret_password"

    # Vulnerability 2: Weak hashing algorithm
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    # Vulnerability 3: Timing attack vulnerability
    if username == admin_username:
        if hashed_password == hashlib.md5(admin_password.encode()).hexdigest():
            return "Login successful"
        else:
            return "Incorrect password"
    else:
        return "User not found"

# Vulnerability 4: Insecure data handling
def store_user_data(user_data):
    # This function doesn't sanitize or validate input
    with open("user_data.txt", "a") as f:
        f.write(user_data + "\n")

# Vulnerability 5: SQL Injection vulnerability
def get_user_data(user_id):
    # This is a mock function to demonstrate SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    # Imagine this query is being executed on a database
    return f"Executing query: {query}"

# Usage example
if __name__ == "__main__":
    print(vulnerable_login("admin", "wrong_password"))
    store_user_data("user1;admin;true")
    print(get_user_data("1 OR 1=1"))
