# reports.py
from models import get_transactions, get_transactions_by_type, get_transactions_by_category

def generate_report():
    transactions = get_transactions()
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = income - expenses
    
    print(f'Total Income: ${income:.2f}')
    print(f'Total Expenses: ${expenses:.2f}')
    print(f'Balance: ${balance:.2f}')

def generate_category_report(category):
    transactions = get_transactions_by_category(category)
    total = sum(t['amount'] for t in transactions)
    
    print(f'Total for {category}: ${total:.2f}')
