import func as f

total = 0.0

while True:
    print(f"""Welcome to the Finance Tracker! Please select an option from the menu below (Input the corresponding number):
    1. Input Expense
    2. Input Income
    3. View Transaction Summary
    4. View Total Income
    5. View Total Expenses
    6. View Current Balance
    7. Exit
    """)
    choice = input("Enter your choice: ")

# Begin checking the user's choice and calling the appropriate function
    if choice == '7':
        print("Exiting the Finance Tracker. Goodbye!")
        break

    if choice == '1':
        print(f"You have selected to input an expense. Please provide the following details:")
        expense_amount = float(input("Enter the expense amount: $"))
        expense_category = input("Enter the expense category (e.g., Food, Transport, Utilities): ")
        expense_date = input("Enter the date of the expense (YYYY-MM-DD): ")
        total -=f.add_expense(expense_amount, expense_category, expense_date)
        print(f"Total balance after adding expense: ${total}")

    if choice == '2':
        print(f"You have selected to input income. Please provide the following details:")
        income_amount = float(input("Enter the income amount: $"))
        income_source = input("Enter the income source (e.g., Salary, Freelance, Investment): ")
        income_date = input("Enter the date of the income (YYYY-MM-DD): ")
        total += f.add_income(income_amount, income_source, income_date)
        print(f"Total balance after adding income: ${total}")