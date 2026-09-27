from storage import load_expenses, save_expenses
from validation import valid_amount, valid_text


def add_expense():

    expenses = load_expenses()

    amount = input("Enter amount: ")

    if not valid_amount(amount):
        print("Invalid amount.")
        return

    category = input("Enter category: ")

    if not valid_text(category):
        print("Invalid category.")
        return

    date = input("Enter date: ")

    if not valid_text(date):
        print("Invalid date.")
        return

    description = input("Enter description: ")

    if not valid_text(description):
        print("Invalid description.")
        return

    new_expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    expenses.append(new_expense)

    save_expenses(expenses)

    print("Expense added successfully!")


def update_expense():

    expenses = load_expenses()

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i in range(len(expenses)):
        print(i + 1, expenses[i])

    number = int(input("Enter expense number to update: "))

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return

    index = number - 1

    amount = input("Enter new amount: ")

    if not valid_amount(amount):
        print("Invalid amount.")
        return

    category = input("Enter new category: ")
    date = input("Enter new date: ")
    description = input("Enter new description: ")

    expenses[index]["amount"] = amount
    expenses[index]["category"] = category
    expenses[index]["date"] = date
    expenses[index]["description"] = description

    save_expenses(expenses)

    print("Expense updated successfully!")


def delete_expense():

    expenses = load_expenses()

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i in range(len(expenses)):
        print(i + 1, expenses[i])

    number = int(input("Enter expense number to delete: "))

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return

    expenses.pop(number - 1)

    save_expenses(expenses)

    print("Expense deleted successfully!")