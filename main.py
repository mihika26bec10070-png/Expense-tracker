from expense import add_expense, update_expense, delete_expense
from display import show_expenses
from analysis import show_total, category_analysis
from config import APP_NAME


print("================================")
print(APP_NAME)
print("================================")


while True:

    print("\n----- MENU -----")
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
        show_expenses()

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