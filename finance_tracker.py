import func as f

total = 0.0
data_matrix = []

while True:
    print(f"""Welcome to the Finance Tracker! Please select an option from the menu below (Input the corresponding number):
    1. Input Expense
    2. Input Income
    3. View Transactions Summary
    4. View Total Income
    5. View Total Expenses
    6. View Current Balance
    7. Exit
    """)
    choice = input("Enter your choice: ")

# Begin checking the user's choice and executing the corresponding functionality
    if choice == '7':
        print("Exiting the Finance Tracker. Goodbye!")
        break

    if choice == '1':
        print(f"You have selected to input an expense. Please provide the following details:")
        expense_amount = float(input("Enter the expense amount: $"))
        data_matrix.append([])
        data_matrix[len(data_matrix) - 1].append('Expense')
        data_matrix[len(data_matrix) - 1].append(expense_amount)
        expense_category = input("Enter the expense category (e.g., Food, Transport, Utilities): ")
        data_matrix[len(data_matrix) - 1].append(expense_category)
        expense_date = input("Enter the date of the expense (YYYY-MM-DD): ")
        data_matrix[len(data_matrix) - 1].append(expense_date)
        total -= f.expense_total(expense_amount, expense_category, expense_date)
        data_matrix[len(data_matrix) - 1].append(total)
        print(f"Total balance after adding expense: ${total}")

    if choice == '2':
        print(f"You have selected to input income. Please provide the following details:")
        income_amount = float(input("Enter the income amount: $"))
        income_source = input("Enter the income source (e.g., Salary, Freelance, Investment): ")
        income_date = input("Enter the date of the income (YYYY-MM-DD): ")
        data_matrix.append([])
        data_matrix[len(data_matrix) - 1].append('Income')
        data_matrix[len(data_matrix) - 1].append(income_amount)
        data_matrix[len(data_matrix) - 1].append(income_source)
        data_matrix[len(data_matrix) - 1].append(income_date)
        total += f.income_total(income_amount, income_source, income_date)
        data_matrix[len(data_matrix) - 1].append(total)
        print(f"Total balance after adding income: ${total}")

    if choice == '3':
        print("Transactions Summary:")
        for transaction in data_matrix:
            print(f"Type: {transaction[0]}, Amount: ${transaction[1]}, Category/Source: {transaction[2]}, Date: {transaction[3]}")
            print(f"Balance after transaction: ${transaction[4]}")

    if choice == '4':
        print(f"Total Income: ${sum(transaction[1] for transaction in data_matrix if transaction[0] == 'Income')}")

    if choice == '5':
        print(f"Total Expenses: ${sum(transaction[1] for transaction in data_matrix if transaction[0] == 'Expense')}")

    if choice == '6':
        print(f"Current Balance: ${total}")