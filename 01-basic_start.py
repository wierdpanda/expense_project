expense_name = []
expense_amount = []

while True:
    print("\nWelcome to Nat's expense tracker")
    print("1. Add expense name + amount")
    print("2. View expenses")
    print("3. View total spent")
    print("4. Exit program")

    choice = input("Please select an option: ")

    if choice == "1":
        while True:
            user_input = input("\nEnter expense name and amount (or q): ")

            if user_input == "q":
                break

            parts = user_input.split()

            if len(parts) != 2:
                print("Please enter exactly 2 values (item amount)")
                continue

            name = parts[0]
            amount = parts[1]

            if not amount.isdigit():
                print("\nAmount must be a number")
                continue

            expense_name.append(name)
            expense_amount.append(int(amount))

            print(f"\nAdded {name} with amount {amount}")

    elif choice == "2":
        print("\nExpenses:")
        for i in range(len(expense_name)):
            print(f"{expense_name[i]} - {expense_amount[i]}")

    elif choice == "3":
        total = sum(expense_amount)
        print(f"\nTotal spent: {total}")

    elif choice == "4":
        print("Goodbye!")
        break