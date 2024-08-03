# Personal Finance Tracker

This Python script helps you track your personal finances, including income and expenses. It allows you to categorize transactions and generate reports.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Mamir21/personal-finance-tracker.git
    ```

2. **Navigate to the project directory**:
    ```sh
    cd personal-finance-tracker
    ```

3. **Set up the database**:
    ```sh
    python db.py
    ```

4. **Run the script**:
    ```sh
    python finance_tracker.py
    ```

## Files

- **db.py**: This file sets up the database for storing transactions. It creates the necessary tables and initializes the database.
- **finance_tracker.py**: This is the main script to run the personal finance tracker application. It includes the main menu and user interface.
- **models.py**: This file defines the data models for the transactions, including income and expense categories.
- **reports.py**: This file contains functions to generate various financial reports, such as total income, total expenses, and category-specific reports.

## Customization

- **Database Configuration**: If you need to change the database settings, you can modify the `db.py` file to configure the database connection and table structures.
- **Categories**: To add or remove categories, update the `models.py` file to reflect the changes in the category model.
- **Report Generation**: You can customize the report formats and contents by editing the functions in the `reports.py` file.

## Options

- **Add Transaction**: Add a transaction with date, category, amount, and type (income or expense).
- **Generate Report**: Generate a financial report for total income, total expenses, and balance.
- **Category Report**: Generate a report for a specific category.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
