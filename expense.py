import json
import os

# ================
# File settings
# ================

SAVE_FILE = "save_state_expense.json"


# =====================
# CLEAR SAVE PROMPT
# =====================

while True:
    choice = input("Do you wish to load previous save data? (Y/N) " \
    "\nNote failure to load previous data will result in deleting old data and starting from scratch\n").lower()
    if choice == "n":
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)
            print("🗑️ Save data has been deleted.")
            break
        else:
            print("ℹ️ No save file to delete.")
            break
    elif choice =="y":
        print("Continueing with existing data.")
        break
    else:
        print("please type 'y' or 'n'.")    



# =====================
# LOAD STATE
# =====================

def load_state():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            data = json.load(file)
        print("✅Loaded saved data")
        return data["expenses"]

    else:
        print("⚠️ No save file found. Starting fresh.")
        expenses = []
        return expenses

# =====================
# SAVE STATE
# =====================
def save_state(expenses):
    data = {
        "expenses": expenses}
    with open(SAVE_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print(f"💾 State saved to {os.path.abspath(SAVE_FILE)}")


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Main program start

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>


#1 list within list to link variables together
expenses = load_state()


#Outer loop for main program
while True:
    print("\nWelcome to Nat's expense tracker")
    print("1. Add expense name, amount and Category")
    print("2. View expenses")
    print("3. View total spent")
    print("4. Exit program")

    choice = input("Please select an option: ")


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #inner loop for adding a name + expense amount + category

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if choice == "1":
        while True:
            user_input = input("\nEnter expense name, amount and category (or q to return to previous menu): ")
            #back to previous menu input
            if user_input == "q":
                break

            parts = user_input.split()
            #name and amount input
            if len(parts) != 3:
                print("\nPlease enter exactly 3 values (item amount)")
                continue

            name = parts[0]
            amount = parts[1]
            category = parts[2]

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            #Rules for amount  inputs  START

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            #ensure amount input is a number
            if not amount.lstrip("-").isdigit():
                print("\nAmount must be a number")
                continue
            amount = int(amount) 
            # ensure amount is above 0
            if amount <=0:
                print("\nAmount must be above 0")
                continue

        


            #putting both variables into 1 list

            expenses.append([name, int(amount), category])

            print(f"\nAdded {name} with amount R{amount} in the {category} category")
    #choice 2 to view all expenses under each other
    elif choice == "2":
        print("\nExpenses:")
        for expense in expenses:
            print(f"{expense[0]} - R{expense[1]} on {expense[2]}")



    #view the total amount for alL expenses     
    elif choice == "3":
        total = 0

        print("\n1. Total for each category")
        print("2. Total for all expenses")

        expense_choice=input("Please select an option:")

        #each category with its total expense
        if expense_choice == "1":
            print("We are still working on this option please select option 2 until we have implemented this feature")

        elif expense_choice == "2":    
            for expense in expenses:
                total += expense[1]
            print(f"\nTotal spent: R{total} \n")
            print("Returning to main menu.\n")
    #this closes the program
    elif choice == "4":
        save_state(expenses)
        print("Goodbye!")
        break