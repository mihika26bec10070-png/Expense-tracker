expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expenses.append([name, amount])
    print("Expense added successfully!")

def show_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("\nYour Expenses:")
        for expense in expenses:
            print(expense[0], ":", expense[1])

def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense[1]

    print("Total Expense =", total)


while True:
    print("\n----- EXPENSE TRACKER -----")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        show_expenses()

    elif choice == 3:
        total_expense()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")