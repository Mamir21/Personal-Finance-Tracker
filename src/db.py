# db.py
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('finance_tracker.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    with get_db_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY,
                            date TEXT NOT NULL,
                            category TEXT NOT NULL,
                            amount REAL NOT NULL,
                            type TEXT NOT NULL
                        )''')

if __name__ == '__main__':
    create_tables()
