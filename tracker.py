import json
import os
from datetime import date

DATA_FILE = "data.json"



def load_expenses():

    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_expenses(expenses):

    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):

    print("\n--- Add Expense ---")


    while True:
        try:
            amount = float(input("Enter amount (example: 12.50): "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number like 12.50.")

    category = input("Enter category (Food / Transport / Shopping): ").strip()
    description = input("Enter description: ").strip()


    user_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if user_date == "":
        expense_date = str(date.today())
    else:
        expense_date = user_date

    expense = {
        "date": expense_date,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added!\n")


def view_expenses(expenses):
    """Print all expenses."""
    print("\n--- All Expenses ---")
    if len(expenses) == 0:
        print("No expenses found.\n")
        return

    for e in expenses:
        print(f"{e['date']} | {e['category']:<10} | ${e['amount']:.2f} | {e['description']}")
    print()


def summary(expenses):
    """Show total spent + total per category."""
    print("\n--- Summary ---")
    if len(expenses) == 0:
        print("No expenses to summarize.\n")
        return

    total = 0
    category_totals = {}

    for e in expenses:
        total += e["amount"]

        cat = e["category"]
        if cat not in category_totals:
            category_totals[cat] = 0
        category_totals[cat] += e["amount"]

    print(f"Total spent: ${total:.2f}\n")
    print("By category:")
    for cat in category_totals:
        print(f"{cat:<10}: ${category_totals[cat]:.2f}")
    print()


def filter_by_category(expenses):

    print("\n--- Filter by Category ---")
    if len(expenses) == 0:
        print("No expenses found.\n")
        return

    wanted = input("Enter category to filter by: ").strip()

    found = False
    for e in expenses:
        if e["category"].lower() == wanted.lower():
            print(f"{e['date']} | {e['category']:<10} | ${e['amount']:.2f} | {e['description']}")
            found = True

    if not found:
        print("No expenses found in that category.")
    print()


# main program

def main():
    expenses = load_expenses()

    while True:
        print("=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Summary (totals)")
        print("4. Filter by category")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary(expenses)
        elif choice == "4":
            filter_by_category(expenses)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid option. Pick 1-5.\n")


if __name__ == "__main__":
    main()


