
expenses = []


# Add Expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    expenses.append(expense)
    print("Expense added successfully!")


# View Expenses
def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n----- EXPENSES -----")

    for i in range(len(expenses)):
        print("\nExpense", i + 1)
        print("Amount:", expenses[i]["amount"])
        print("Category:", expenses[i]["category"])
        print("Date:", expenses[i]["date"])
        print("Description:", expenses[i]["description"])


# Update Expense
def update_expense():
    view_expenses()

    if len(expenses) == 0:
        return

    number = int(input("\nEnter expense number to update: "))

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return

    index = number - 1

    expenses[index]["amount"] = float(input("Enter new amount: "))
    expenses[index]["category"] = input("Enter new category: ")
    expenses[index]["date"] = input("Enter new date: ")
    expenses[index]["description"] = input("Enter new description: ")

    print("Expense updated successfully!")


# Delete Expense
def delete_expense():
    view_expenses()

    if len(expenses) == 0:
        return

    number = int(input("\nEnter expense number to delete: "))

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return

    expenses.pop(number - 1)

    print("Expense deleted successfully!")


# Calculate Total
def show_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense =", total)


# Category Analysis
def category_analysis():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] = categories[category] + amount
        else:
            categories[category] = amount

    print("\n----- CATEGORY ANALYSIS -----")

    for category in categories:
        print(category, "=", categories[category])


# Main Program
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Show Total Expense")
    print("6. Category Analysis")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        update_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        show_total()

    elif choice == "6":
        category_analysis()

    elif choice == "7":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")