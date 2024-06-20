import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Expenses tracker')
# Get current date
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")

# Function to select a sheet
def select_sheet() -> object:
    """
    This function helps you choose which sheet to access from your Google Spreadsheet.

    It will keep asking you to pick an option until you give a valid choice. Here are the options:
    - Press "1" for the "Incomes" sheet
    - Press "2" for the "Expenses" sheet
    - Press "3" for the "Summary" sheet

    Once you make a choice, the function will select the corresponding sheet, let you know it's selected,
    and then return that sheet so you can work with it.

    Returns:
        The worksheet object you selected from the Google Spreadsheet.
    """
    while True:
        choice = input("Please select the sheet you want to access by entering the corresponding number:\n"
            "1 - Incomes\n"
            "2 - Expenses\n"
            "3 - Summary\n"
            "0 - Exit the program\n"
            ">> ")
        if choice in ["0", "1", "2", "3"]:
            if choice == "1":
                print("Selecting Incomes sheet...")
                incomes = SHEET.worksheet("Incomes")
                print("Incomes sheet selected.")
                print("")
                return incomes
            elif choice == "2":
                print("Selecting Expenses sheet...")
                expenses = SHEET.worksheet("Expenses")
                print("Expenses sheet selected.")
                print("")
                return expenses
            elif choice == "3":
                print("Selecting Summary sheet...")
                summaries = SHEET.worksheet("Summary")
                print("Summary sheet selected.")
                print("")
                return summaries
            else:
                print("Exiting the program...")
                return None
        else:
            print("Wrong Entry!!!")

#Function to validate data entry
def validate_data_entry(data) -> bool:
    """
    Validates the provided data based on type-specific criteria.

    Parameters:
        data (str or float): The data to be validated.

    Returns:
        bool: True if the data meets the validation criteria, False otherwise.
    """
    if isinstance(data, str):
        if len(data) > 50:
            print("The length of this entry cannot exceed 50 characters.")
            return False
        if len(data) < 4:
            print("The length of this entry cannot be less than 4 characters.")
            return False
        if data.isdigit():
            print("Only digits are not allowed.")
            return False
        if data.isspace():
            print("Only space is not allowed.")
            return False
    if isinstance(data, float):
        if data < 1:
            print("Please enter a valid amount.")
            return False
    return True


#Function to update or display a sheet
def modify_or_display_sheet(sheet: object) -> list:
    """
    This function allows you to either show the sheet data or add new data to the sheet.

    Parameters:
        sheet: The worksheet object you want to manage.

    Returns:
        list: A list containing two elements:
              - Total incomes (int)
              - Total expenses (int)
    """
    if sheet.title != "Summary":
        print("Select an action: view the sheet's data or add new data?\n"
            "Type 'info' to see the data or 'add' to enter new data.\n"
            "If you want to close the current sheet type 'exit'.\n"
            )
    else:
        print("Select an action: Type 'info' to view the sheet's data or\n"
            "Type 'exit' to close the sheet.\n"
            )

    # Data list to store in sheets
    data_list = []

    # List that store sum of total expenses and sum of total incomes
    total_incomes_total_expenses = []

    while True:
        user_choice = input(">>  ").lower()
        if user_choice in ["info", "add", "exit"]:
            if user_choice == "info":
                data = sheet.get_all_values()

                # Validate if sheet is empty
                if not data[1:]:
                    if sheet.title != "Summary":
                        print("Sheet is empty!\nType 'add' to add data in this sheet or 'exit' to exit the current sheet.")
                    else:
                        print("Sheet is empty!\nType 'exit' to exit the current sheet.")
                else:
                    print("Presenting the data...")
                    print("")
                    print(data)
                    print("")
                    if sheet.title != "Summary":
                        print("Current data shown. Type 'add' to add more data or 'exit' to close the sheet.")
                    else:
                        print("Current data shown. Type 'exit' to close the sheet.")
            elif user_choice == "add":
                if sheet.title == "Summary":
                    print("Heads up: This sheet does not support manual data addition.\n"
                          "This sheet is read-only. Type 'info' to see its contents."
                          )
                elif sheet.title == "Incomes":
                    print("You need to specify: Source, Amount, Payment Method, and Description.")
                    print("Example: Source (Job salary), Amount (4000)," 
                          "Payment method (Card, Cash), Description (Salary from online job)."
                          )  
                    print("")
                    # append current date to data list as the first element of the list
                    data_list.append(CURRENT_DATE)
                    # Move every inputs inside while loop 
                    # If data is invalid repeat inputs
                    while True:
                        source = input("Enter income source\n>>  ").capitalize() 
                        if validate_data_entry(source):
                            data_list.append(source)
                            break
                    while True:
                        try:
                            amount = float(input("Enter income amount\n>>  ")) 
                            if validate_data_entry(amount):
                                data_list.append(amount)
                                break
                        except ValueError:
                            print("Please enter a valid number for the amount.")
                    while True:
                        payment_method = input("Enter income Payment method\n>>  ").capitalize()
                        if validate_data_entry(payment_method):
                            data_list.append(payment_method)
                            break
                    while True:
                        description = input("write a description for this income\n>>  ").capitalize()
                        if validate_data_entry(description):
                            data_list.append(description)
                            break
                    print("Adding data to incomes sheet...")
                    sheet.append_row(data_list)
                    data_list.clear()
                    print("Your inputs has been successfully saved in the worksheet.")
                    print("")

                    print("Calculating remaining balance...")
                    print("")
                    # Accessing amount column of the sheet to return sum of all amounts
                    incomes_amount_column = sheet.col_values(3)
                    incomes_amount_values = incomes_amount_column[1:]
                    sum_of_incomes_amount_values = sum(float(value) for value in incomes_amount_values)
                    # Append total incomes to the list
                    total_incomes_total_expenses.append(sum_of_incomes_amount_values)

                    # Access sum of expenses amount
                    expenses_sheet = SHEET.worksheet("Expenses")
                    ex_amount_column = expenses_sheet.col_values(3)
                    ex_amount_values = ex_amount_column[1:]
                    sum_of_ex_amount_values = sum(float(value) for value in ex_amount_values)
                    # Append existing total expenses to the list
                    total_incomes_total_expenses.append(sum_of_ex_amount_values)
                    print("Summary sheet updated successfully.")
                    return total_incomes_total_expenses
                elif sheet.title == "Expenses":
                    # Access incomes sheet 
                    incomes_sheet = SHEET.worksheet("Incomes")
                    # Validate if incomes sheet is empty
                    # Do not allow expenses sheet to have data entry ability
                    if not incomes_sheet.get_all_values()[1:]:
                        print("Sorry, you do not have any incomes to add an expense!\nType 'exit' to exit the current sheet.")
                    else:
                        print("You need to specify: Type, Amount, Payment Method, and Description.")
                        print("Example: Type (Electric bill), Amount (450)," 
                            "Payment method (Card, Cash), Description (This payment is for the electricity expenses.)."
                            )  
                        print("")
                        # append current date to data list as the first element of the list
                        data_list.append(CURRENT_DATE)
                        # Move every inputs inside while loop 
                        # If data is invalid repeat inputs
                        while True:
                            expense_type = input("Enter expense type\n>>  ").capitalize()
                            if validate_data_entry(expense_type):
                                data_list.append(expense_type)
                                break
                        while True:
                            try:
                                amount = float(input("Enter expense amount\n>>  ")) 
                                if validate_data_entry(amount):
                                    data_list.append(amount)
                                    break
                            except ValueError:
                                print("Please enter a valid number for the amount.")
                        while True:
                            payment_method = input("Enter expense Payment method\n>>  ").capitalize()
                            if validate_data_entry(payment_method):
                                data_list.append(payment_method)
                                break
                        while True:
                            description = input("write a description for this expense\n>>  ").capitalize()
                            if validate_data_entry(description):
                                data_list.append(description)
                                break
                        print("Adding data to expenses sheet...")
                        sheet.append_row(data_list)
                        data_list.clear()
                        print("Your inputs has been successfully saved in the worksheet.")
                        print("")
                        
                        print("Calculating remaining balance...")
                        print("")
                        # Access sum of incomes amount
                        inc_amount_column = incomes_sheet.col_values(3)
                        inc_amount_values = inc_amount_column[1:]
                        sum_of_inc_amount_values = sum(float(value) for value in inc_amount_values)
                        # Append existing total incomes to the list
                        total_incomes_total_expenses.append(sum_of_inc_amount_values)

                        # Accessing amount column of the sheet to return sum of all amounts
                        expenses_amount_column = sheet.col_values(3)
                        expenses_amount_values = expenses_amount_column[1:]
                        sum_of_expenses_amount_values = sum(float(value) for value in expenses_amount_values)
                        # Append total expenses to the list
                        total_incomes_total_expenses.append(sum_of_expenses_amount_values)
                        print("Summary sheet updated successfully.")
                        return total_incomes_total_expenses         
            else:
                print("Closing the sheet...\nSheet cloesed.")
                break
        else:
            if sheet.title != "Summary":
                print("Wrong Entry!!!\nPlease type 'info', 'add' or 'exit'.")
            else:
                print("wrong Entry!!!\nPlease type 'info' or 'exit'.") 
        
def update_remaining_balance(totals: list):
    """
    Update the remaining balance in the Summary sheet based on the total incomes and total expenses.

    Parameters:
        totals (list): A list containing two elements:
                       - Total incomes (int)
                       - Total expenses (int)
    """
    if totals:
        total_incomes = totals[0]
        total_expenses = totals[1]
        summary_sheet = SHEET.worksheet("Summary")
        summary_sheet.append_row([CURRENT_DATE, total_incomes, total_expenses, total_incomes - total_expenses])

    
def main():
    """
    Run all program functions
    """
    print("****Welcome to Expenses Tracker! We're here to help you track your expenses and incomes.****\n****Let's begin your financial journey.****")
    while True:
        selected_sheet = select_sheet()
        if selected_sheet:
            totals = modify_or_display_sheet(selected_sheet)
            if totals:
                update_remaining_balance(totals)
        else:
            print("")
            print("Thank you for using the Expenses Tracker. Goodbye!")
            break

main()
