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

# ==================
# Helper Functions
# ==================
def show_all_expenses():
    
    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    for expense in expenses:
        print(f"ID:{expense[0]} | {expense[1]} - R{expense[2]} on {expense[3]}")


def show_expenses_by_category(selected_category):

    cursor.execute(
        """
        SELECT * FROM expenses
        WHERE category = ?
        """,
        (selected_category,)
    )

    filtered_expenses = cursor.fetchall()

    for expense in filtered_expenses:
        print(f"ID:{expense[0]} | {expense[1]} - R{expense[2]} on {expense[3]}")    
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
    print("4. Edit and update current expenses")
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
    
            number_count = 1

            cursor.execute(
                "SELECT DISTINCT category FROM expenses"
            )

            categories = cursor.fetchall()

            for category in categories:
                print(f"{number_count}. {category[0]}")
                number_count += 1

            choice = int(input("Please select category via a number: "))

            selected_category = categories[choice - 1][0]

            show_expenses_by_category(selected_category)

        # BELOW IS CODE TO BE REPLACE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # if choice == "1":
                      
        #     # sql loop to find and select categories
        #     number_count = 1
        #     cursor.execute(
        #         "SELECT DISTINCT category FROM expenses"
        #     )

        #     categories = cursor.fetchall()

        #     # For loop which creates the visible list for the user.
        #     for category in categories:
        #         print(f"{number_count}. {category[0]}")

        #         number_count += 1

            
           
           
                
        #     choice = int(input("please select category via a number or "))
           
        #     selected_category = categories[choice -1][0]
 
        #     cursor.execute(
        #         """
        #         SELECT * FROM expenses
        #         WHERE category = ?
        #         """,
        #         (selected_category,)
        #     )

        #     filtered_expenses = cursor.fetchall()
        #     for expense in filtered_expenses:
        #         print(f"ID:{expense[0]} | {expense[1]}- R{expense[2]} on {expense[3]}")  

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   

              
        # ==================================
        # CHOICE 2. View individual expenses
        # SUBCHOICE 2.view all expenses
        # ==================================
        elif choice == "2":
    
            show_all_expenses()




            # BELOW IS CODE TO BE REPLACE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            # cursor.execute("SELECT * FROM expenses")

            # expenses = cursor.fetchall()

            # for expense in expenses:
            #     print(f"ID:{expense[0]} | {expense[1]} - R{expense[2]} on {expense[3]}")
            # BELOW IS CODE TO BE REPLACE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<            


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





    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
    #Choice 4. lets the user update current entrries in the database.    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    elif choice == "4":
        print("\n1.Pick a category of expenses")
        print("2.View all expenses")
        print("q to return to main menu")
        choice = input("\nPlease select an option: \n")

        
        # =====================================
        # CHOICE 4. View individual expenses
        # SUBCHOICE q to return to main menu
        # =====================================
        if input == "q":
                break
        

        # =====================================
        # CHOICE 4. View individual expenses
        # SUBCHOICE 1.pick a category of expenses
        # =====================================
        elif choice == "1":


            number_count = 1

            cursor.execute(
                "SELECT DISTINCT category FROM expenses"
            )

            categories = cursor.fetchall()

            for category in categories:
                print(f"{number_count}. {category[0]}")
                number_count += 1

            choice = int(input("Please select category via a number: "))

            selected_category = categories[choice - 1][0]

            show_expenses_by_category(selected_category)

            # ---------------------------------------------------------------------------------------------------------------
            # This  isolates and checks if the id exists and returns a prompt to the user saying it does or does not exist
            # ---------------------------------------------------------------------------------------------------------------
            expense_id = input("Please select an ID to update")
            cursor.execute(
            """
            SELECT * FROM expenses
            WHERE id = ?
            AND category = ?
            """,
            (expense_id, selected_category)
            )

            expense = cursor.fetchone()

            if expense:

                print("\nExpense Found:")
                print(f"ID: {expense[0]}")
                print(f"Name: {expense[1]}")
                print(f"Amount: R{expense[2]}")
                print(f"Category: {expense[3]}")

                print("\nEnter the new values below.")

                new_name = input("Enter new name: ")

                new_amount = input("Enter new amount: ")

                if not new_amount.isdigit():
                    print("Amount must be a number.")
                    continue

                new_amount = int(new_amount)

                if new_amount <= 0:
                    print("Amount must be above 0.")
                    continue

                new_category = input("Enter new category: ").lower()

                cursor.execute(
                """
                UPDATE expenses
                SET name = ?, amount = ?, category = ?
                WHERE id = ?
                """,
                (new_name, new_amount, new_category, expense_id)
                )

                conn.commit()

                print("\nExpense updated successfully!")

                cursor.execute(
                """
                SELECT * FROM expenses
                WHERE id = ?
                """,
                (expense_id,)
                )

                updated_expense = cursor.fetchone()

                print("\nUpdated Expense:")
                print(
                f"ID:{updated_expense[0]} | "
                f"{updated_expense[1]} - "
                f"R{updated_expense[2]} on "
                f"{updated_expense[3]}"
                )
            else:
                print("Expense not found")

        # ==================================
        # CHOICE 4. View individual expenses
        # SUBCHOICE 2.view all expenses
        # ==================================
        elif choice == "2":    

            show_all_expenses()


            # ---------------------------------------------------------------------------------------------------------------
            # This  isolates and checks if the id exists and returns a prompt to the user saying it does or does not exist
            # ---------------------------------------------------------------------------------------------------------------
            expense_id = input("Please select an ID to update or q to return to main menu")
            cursor.execute(
                """
                SELECT * FROM expenses
                WHERE id = ?
                """,
                (expense_id,)  
            )

            expense = cursor.fetchone()
            
            if expense:     #this means:  if expense is not None:
                print("\nExpense Found:")
                
                print(f"ID: {expense[0]}")
                print(f"Name: {expense[1]}")
                print(f"Amount: R{expense[2]}")
                print(f"Category: {expense[3]}")

                print("\nEnter the new values below.")

                new_name = input("Enter new name: ")

                new_amount = input("Enter new amount: ")

                if not new_amount.isdigit():
                    print("Amount must be a number.")
                    continue
                new_amount = int(new_amount)

                if new_amount <= 0:
                    print("Amount must be above 0")
                    continue

                new_category = input("Enter new category: ").lower()

                cursor.execute(
                """
                UPDATE expenses
                SET name = ?, amount = ?, category = ?
                WHERE id = ?
                """,
                (new_name, new_amount, new_category, expense_id)
                )

                conn.commit()

                print("\nExpense updated successfully!")

                cursor.execute(
                """
                SELECT * FROM expenses
                WHERE id = ?
                """,
                (expense_id,)
                )

                updated_expense = cursor.fetchone()

                print("\nUpdated Expense:")
                print(
                f"ID:{updated_expense[0]} | "
                f"{updated_expense[1]} - "
                f"R{updated_expense[2]} on "
                f"{updated_expense[3]}"
                )
                
            else:
                print("Expense not found")


        # ===============
        # Shows expenses and asks user to select an id to delete
        # =============== 

        # show all expenses
        # ask for an ID
        # check wether ID exists
        #print expenses found










    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
    #Choice q ends and closes program    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>          
    
    elif choice == "q":
        print("Goodbye!")
        break

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
    #this forces numbered choices or q/Q to quit    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    else: 
        print("Please select a number from 1-5 or q/Q")





