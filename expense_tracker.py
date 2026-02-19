import csv

# Function to add expense
def add_expense(desc, amount):
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])
    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            print("\n--- Expense List ---")
            for row in reader:
                print(f"Item: {row[0]}, Amount: ₹{row[1]}")
    except FileNotFoundError:
        print("No expenses found. Add some first!\n")

# Function to calculate total expenses
def total_expenses():
    total = 0
    try:
        with open("expenses.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                total += int(row[1])
        print(f"\nTotal Expenses: ₹{total}\n")
    except FileNotFoundError:
        print("No expenses to calculate.\n")

# Main menu loop
while True:
    print("====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spent")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        desc = input("Enter expense description: ")
        amount = input("Enter amount: ")
        add_expense(desc, amount)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice. Try again.\n")


# ---------------- EXPECTED OUTPUT ----------------

====== Expense Tracker ======
1. Add Expense
2. View Expenses
3. View Total Spent
4. Exit
Enter your choice (1-4): 1
Enter expense description: Food
Enter amount: 200
Expense added successfully!

====== Expense Tracker ======
1. Add Expense
2. View Expenses
3. View Total Spent
4. Exit
Enter your choice (1-4): 2

--- Expense List ---
Item: Food, Amount: ₹200

====== Expense Tracker ======
1. Add Expense
2. View Expenses
3. View Total Spent
4. Exit
Enter your choice (1-4): 3

Total Expenses: ₹200

====== Expense Tracker ======
1. Add Expense
2. View Expenses
3. View Total Spent
4. Exit
Enter your choice (1-4): 4
Exiting... Thank you!
