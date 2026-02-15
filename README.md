# Task2
##Python Internship Task 2 - Expense Tracker using CSV and File Handling
# Task 2 - Expense Tracker

## 📌 Project Description
This is a Python CLI based Expense Tracker application.
It allows the user to:
- Add expenses
- View all expenses
- Calculate total expenses
- Store data in a CSV file

---

## 🚀 Features
- Uses Python functions
- Uses CSV file handling
- Menu-driven program
- Simple and easy to use

---

## 🧠 Python Code

```python
import csv
import os

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Description", "Amount"])

def add_expense():
    desc = input("Enter expense description: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])

    print("Expense added successfully!\n")

def view_expenses():
    print("\n--- All Expenses ---")
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(f"Item: {row[0]} | Amount: ₹{row[1]}")
    print()

def total_expenses():
    total = 0
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            total += float(row[1])

    print(f"\nTotal Expenses: ₹{total}\n")

def menu():
    while True:
        print("====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

initialize_file()
menu()

sample output


====== EXPENSE TRACKER ======
1. Add Expense
2. View Expenses
3. View Total Expenses
4. Exit
Choose an option (1-4): 1

Enter expense description: Coffee
Enter amount: 50
Expense added successfully!

Choose an option (1-4): 3

Total Expenses: ₹50.0
