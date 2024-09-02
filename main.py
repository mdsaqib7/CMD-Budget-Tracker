expenses = []


def add_expenses():
    description = input("Enter the expense description: ")
    while True:
        try:
            amount = float(input("Enter the amount: $"))
            break
        except ValueError:
            print("Enter a valid number.")

    expenses.append({"description": description, "amount": amount})
    print(f"Added expense: {description} - ${amount}\n")


def view_total_amount_spent():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total amount spent: {total:.2f}\n")


def view_expenses():
    if not expenses:
        print("No expenses added yet.")
        return
    print("Your Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['description']} - ${expense['amount']:.2f}")
    print()


def main():
    while True:
        print("=====Budget Tracker=====")
        print("1. Add Expense")
        print("2. View Total Amount Spent")
        print("3. View All Expenses")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_total_amount_spent()
        elif choice == "3":
            view_expenses()
        elif choice == "4":
            print("Exiting Budget Tracker. Goodbye!!!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
