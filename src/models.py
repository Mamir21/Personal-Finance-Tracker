from db.py import get_db_connection

def add_transaction(date, category, amount, type):
    with get_db_connection() as conn:
        conn.execute('''INSERT INTO transactions (date, category, amount, type) 
                        VALUES (?, ?, ?, ?)''', (date, category, amount, type))

def get_transactions():
    with get_db_connection() as conn:
        transactions = conn.execute('SELECT * FROM transactions').fetchall()
        return transactions

def get_transactions_by_type(type):
    with get_db_connection() as conn:
        transactions = conn.execute('SELECT * FROM transactions WHERE type = ?', (type,)).fetchall()
        return transactions

def get_transactions_by_category(category):
    with get_db_connection() as conn:
        transactions = conn.execute('SELECT * FROM transactions WHERE category = ?', (category,)).fetchall()
        return transactions
