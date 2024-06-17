# finance_tracker.py
import argparse
from models import add_transaction, get_transactions
from reports import generate_report, generate_category_report

def main():
    parser = argparse.ArgumentParser(description='Personal Finance Tracker')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a transaction')
    add_parser.add_argument('date', help='Transaction date (YYYY-MM-DD)')
    add_parser.add_argument('category', help='Transaction category')
    add_parser.add_argument('amount', type=float, help='Transaction amount')
    add_parser.add_argument('type', choices=['income', 'expense'], help='Transaction type')

    report_parser = subparsers.add_parser('report', help='Generate a financial report')
    
    category_report_parser = subparsers.add_parser('category_report', help='Generate a category report')
    category_report_parser.add_argument('category', help='Transaction category')

    args = parser.parse_args()

    if args.command == 'add':
        add_transaction(args.date, args.category, args.amount, args.type)
        print('Transaction added successfully.')
    elif args.command == 'report':
        generate_report()
    elif args.command == 'category_report':
        generate_category_report(args.category)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
