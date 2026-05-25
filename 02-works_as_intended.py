
#1 list within list to link variables together
expenses = []

#outer loop for main program
while True:
    print("\nWelcome to Nat's expense tracker")
    print("1. Add expense name + amount")
    print("2. View expenses")
    print("3. View total spent")
    print("4. Exit program")

    choice = input("Please select an option: ")
    #inner loop for adding a name + expense amount
    if choice == "1":
        while True:
            user_input = input("\nEnter expense name and amount (or q): ")
            #back to previous menu input
            if user_input == "q":
                break

            parts = user_input.split()
            #name and amount input
            if len(parts) != 2:
                print("\nPlease enter exactly 2 values (item amount)")
                continue

            name = parts[0]
            amount = parts[1]
            #ensure amount input is a number
            if not amount.lstrip("-").isdigit():
                print("\nAmount must be a number")
                continue
            amount = int(amount) 
            # ensure amount is above 0
            if amount <=0:
                print("\nAmount must be above 0")
                continue

            #putting both amounts into 1 list
            expenses.append([name, int(amount)])

            print(f"\nAdded {name} with amount R{amount}")
    #choice 2 to view all expenses under each other
    elif choice == "2":
        print("\nExpenses:")
        for expense in expenses:
            print(f"{expense[0]} - R{expense[1]}")
    #view the total amount for al expenses     
    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense[1]
        print(f"\nTotal spent: R{total}")
    #this closes the program
    elif choice == "4":
        print("Goodbye!")
        break