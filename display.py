from storage import load_expenses


def show_expenses():

    expenses = load_expenses()

    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n----- ALL EXPENSES -----")

    for i in range(len(expenses)):

        print("\nExpense", i + 1)

        print("Amount:", expenses[i]["amount"])
        print("Category:", expenses[i]["category"])
        print("Date:", expenses[i]["date"])
        print("Description:", expenses[i]["description"])