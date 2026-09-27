import csv
import os

FILE_NAME = "expenses.csv"


def load_expenses():

    expenses = []

    if not os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "w", newline="")
        writer = csv.writer(file)

        writer.writerow([
            "amount",
            "category",
            "date",
            "description"
        ])

        file.close()

        return expenses

    file = open(FILE_NAME, "r", newline="")
    reader = csv.DictReader(file)

    for row in reader:
        expenses.append(row)

    file.close()

    return expenses


def save_expenses(expenses):

    file = open(FILE_NAME, "w", newline="")
    writer = csv.writer(file)

    writer.writerow([
        "amount",
        "category",
        "date",
        "description"
    ])

    for expense in expenses:
        writer.writerow([
            expense["amount"],
            expense["category"],
            expense["date"],
            expense["description"]
        ])

    file.close()