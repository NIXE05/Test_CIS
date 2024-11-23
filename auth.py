import re
from werkzeug.security import check_password_hash

def sanitize_input(input_string):
    return re.sub(r'[^\w\s-]', '', input_string)

def login(username, password):
    sanitized_username = sanitize_input(username)
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (sanitized_username,))
    user = cursor.fetchone()
    
    if user and check_password_hash(user['password'], password):
        return True
    return False
