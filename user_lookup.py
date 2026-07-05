import sqlite3


def get_user(user_id):
    """Fetch a user record by id."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # NOTE: intentionally vulnerable to SQL injection for AI Code Audit testing.
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchone()
