# Importing and connecting sqlite database
import os
import sqlite3

conn = sqlite3.connect("expense.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    amount REAL,
    category TEXT
)
"""
)

conn.commit()
print(os.path.abspath("expenses.db"))





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Main program start

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>


#1 list within list to link variables together


#====================
#Start of Application
#====================
while True:
    print("\nWelcome to Nat's expense tracker")
    print("Only the create and read features of CRUD are currently working with the update and delete features to still be done ")
    print("1. Add expense name, amount and Category")
    print("2. View individual expenses")
    print("3. View total spent")

    print("q. Exit program")

    choice = input("\nPlease select an option: \n").lower()


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #When choice 1 is picked

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # =======================================================================================
    # CHOICE 1. Add expense name, amount and Category
    # SUBCHOICE 1.Enter expense name, amount and category (or q to return to previous menu): 
    # =======================================================================================
    if choice == "1":
        while True:
            user_input = input("\nEnter expense name, amount and category (or q to return to previous menu):")
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

            #-------------------------------

            #Rules for amount  inputs  START

            #-------------------------------

            #ensure amount input is a number
            if not amount.lstrip("-").isdigit():
                print("\nAmount must be a number")
                continue
            amount = int(amount) 
            # ensure amount is above 0
            if amount <=0:
                print("\nAmount must be above 0")
                continue
            
            category = category.lower()
        


            #putting all 3 variables into 1 list

            cursor.execute(
                """
                INSERT INTO expenses (name, amount, category)
                VALUES (?,?,?)
                """,
                (name, amount, category)
            )

            conn.commit()


            print(f"\nAdded {name} with amount R{amount} in the {category} category")



    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        
    #choice 2 to view all expenses under each other
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  


    elif choice == "2":
        print("\n1.Pick a category of expenses")
        print("2.View all expenses")
        print("q to return to main menu")
        choice = input("\nPlease select an option: \n")

        # print(f"DEBUG: choice is '{choice}'")             this is a standard to help see if choice is actualy selected


    # =====================================
    # CHOICE 2. View individual expenses
    # SUBCHOICE q to return to main menu
    # =====================================
        if input == "q":
                break
        
        # =====================================
        # CHOICE 2. View individual expenses
        # SUBCHOICE 1.pick a category of expenses
        # =====================================
        if choice == "1":
                        
            # sql loop to find and select categories
            number_count = 1
            cursor.execute(
                "SELECT DISTINCT category FROM expenses"
            )

            categories = cursor.fetchall()

            # For loop which creates the visible list for the user.
            for category in categories:
                print(f"{number_count}. {category[0]}")

                number_count += 1

            
           
           
                
            choice = int(input("please select category via a number or "))
           
            selected_category = categories[choice -1][0]
 
            cursor.execute(
                """
                SELECT * FROM expenses
                WHERE category = ?
                """,
                (selected_category,)
            )

            filtered_expenses = cursor.fetchall()
            for expense in filtered_expenses:
                print(f"{expense[1]}- R{expense[2]} on {expense[3]}")            

              
        # ==================================
        # CHOICE 2. View individual expenses
        # SUBCHOICE 2.view all expenses
        # ==================================
        elif choice == "2":

            cursor.execute("SELECT * FROM expenses")

            expenses = cursor.fetchall()

            for expense in expenses:
                print(f"{expense[1]} - R{expense[2]} on {expense[3]}")        


    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
    #Choice 3 view the total amount for all expenses    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  


    elif choice == "3":
        total = 0

        print("\n1. Total for each category")
        print("2. Total for all expenses")

        expense_choice=input("Please select an option:")


        # ===============
        # CHOICE 3. View total spent
        # SUBCHOICE 1.Total for each category
        # ===============

        
        if expense_choice == "1":
            
            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # to help with confusion [] is not always for lists
            #   Structure	Meaning of []
            #   List	Position number (index)
            #   Dictionary	Key lookup
            #   String	Character position

            #You're using the dictionary lookup syntax, which happens to use square brackets too.
            # This is one of those Python things that confuses almost everyone the first time they see it. The difference is determined by what the variable is:
            # If expenses is a list, expenses[...] means list indexing.
            # If category_totals is a dictionary, category_totals[...] means key lookup.

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


            cursor.execute(
                """
                SELECT category, SUM(amount) AS total
                FROM expenses
                GROUP BY category
                """,
            )

            results = cursor.fetchall()

            for category, total in results:
                print(f"{category}: R{total}")



           


        # ===============
        # CHOICE 3. View total spent
        # SUBCHOICE 2.Total for all categories
        # ===============        

        elif expense_choice == "2":
            # FIrst simpler way to do it to call with SQL and do math with python
            # expense_total = 0

            # cursor.execute(  
            #     "SELECT * FROM expenses",)
            
            # expenses = cursor.fetchall()
            
            # for expense in expenses:
            #     expense_total += expense[2]
            # print(f"\nTotal spent: R{expense_total} \n")

            # This way lets SQL call and do the math saving processing time + making code neater
            cursor.execute("SELECT SUM(amount) FROM expenses")
            
            expense_total = cursor.fetchone()[0]

            print(f"\nTotal spent: R{expense_total}")
            print("Returning to main menu.\n")







    elif choice == "4":
        print("hello")        

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
    #Choice q ends and closes program    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          
    #this closes the program
    elif choice == "q":
        print("Goodbye!")
        break

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
    #this forces numbered choices or q/Q to quit    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    else: 
        print("Please select a number from 1-5 or q/Q")





