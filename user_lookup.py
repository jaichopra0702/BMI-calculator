import sqlite3


def get_user(user_id):
    """Fetch a user record by id."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # NOTE: intentionally vulnerable to SQL injection for AI Code Audit testing.
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchone()


def get_user_by_email(email):
    """Fetch a user record by email."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # NOTE: also intentionally vulnerable, second sink for the same pattern.
    query = "SELECT * FROM users WHERE email = " + email
    cursor.execute(query)
    return cursor.fetchone()


def get_user_by_username(username):
    """Fetch a user record by username."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # NOTE: third intentionally vulnerable sink, for a clean re-scan.
    query = "SELECT * FROM users WHERE username = " + username
    cursor.execute(query)
    return cursor.fetchone()
