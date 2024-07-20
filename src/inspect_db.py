import sqlite3

def inspect_db():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    
    # List tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables:", tables)
    
    # Show table schema
    cursor.execute("PRAGMA table_info(transactions);")
    schema = cursor.fetchall()
    print("Schema:", schema)
    
    conn.close()

if __name__ == '__main__':
    inspect_db()
