from storage import load_expenses


def show_total():

    expenses = load_expenses()

    total = 0

    for expense in expenses:
        total = total + float(expense["amount"])

    print("Total Expense =", total)


def category_analysis():

    expenses = load_expenses()

    if len(expenses) == 0:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = float(expense["amount"])

        if category in categories:
            categories[category] = categories[category] + amount
        else:
            categories[category] = amount

    print("\n----- CATEGORY ANALYSIS -----")

    for category in categories:
        print(category, "=", categories[category])