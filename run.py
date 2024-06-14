import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from pprint import pprint


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Expenses tracker')


def select_sheet():
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
        choice = input("Please select the sheet you want to access by entering the corresponding number: 1 for Incomes, 2 for Expenses, or 3 for Summary: \n")
        if choice in ["1", "2", "3"]:
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
            else:
                print("Selecting Summary sheet...")
                summaries = SHEET.worksheet("Summary")
                print("Summary sheet selected.")
                print("")
                return summaries
            break
        else:
            print("Wrong Entry!!!")



def modify_or_display_sheet(sheet):
    """
    This function allows you to either show the sheet data or add new data to the sheet.

    Parameters:
        sheet: The worksheet object you want to manage.

    The function will prompt you to choose between viewing the current data or adding new data.
    """
    if sheet.title != "Summary":
        print("Select an action: view the sheet's data or add new data?\n"
            "Type 'info' to see the data or 'add' to enter new data.\n"
            "If you want to exit the program type 'exit'.\n"
            )
    else:
        print("Select an action: Type 'info' to view the sheet's data or\n"
            "Type 'exit' to exit the program.\n"
            )

    # Data list to store in sheets
    data_list = []

    # Get the current system date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # List that store sum of total expenses and sum of total incomes
    total_incomes_total_expenses = []
    while True:
        user_choice = input(">>  ").lower()
        if user_choice in ["info", "add", "exit"]:
            if user_choice == "info":
                data = sheet.get_all_values()
                print("Presenting the data...")
                print("")
                pprint(data)
                print("")
                if sheet.title != "Summary":
                    print("Current data shown. Type 'add' to add more data or 'exit' to leave the program.")
                else:
                    print("Current data shown. Type 'exit' to leave the program.")
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
                    data_list.append(current_date)
                    source = input("Enter income source\n>>  ").capitalize() 
                    data_list.append(source)
                    amount = int(input("Enter income amount\n>>  ")) 
                    data_list.append(amount)
                    payment_method = input("Enter income Payment method\n>>  ").capitalize()
                    data_list.append(payment_method)
                    description = input("write a description for this income\n>>  ").capitalize()
                    data_list.append(description) 
                    print("Adding data to incomes sheet...")
                    sheet.append_row(data_list)
                    data_list.clear()
                    print("Your inputs has been successfully saved in the worksheet.")
                    print("")
                    print("You can add more incomes to this worksheet by typing 'add',"
                          " view the content by typing 'info', or type 'exit' to exit the program."
                          )
                    # Accessing amount column of the sheet to return sum of all amounts
                    incomes_amount_column = sheet.col_values(3)
                    incomes_amount_values = incomes_amount_column[1:]
                    sum_of_incomes_amount_values = sum(int(value) for value in incomes_amount_values)
                    # Append total incomes to the list
                    total_incomes_total_expenses.append(sum_of_incomes_amount_values)

                    # Access sum of expenses amount
                    expenses_sheet = SHEET.worksheet("Expenses")
                    ex_amount_column = expenses_sheet.col_values(3)
                    ex_amount_values = ex_amount_column[1:]
                    sum_of_ex_amount_values = sum(int(value) for value in ex_amount_values)
                    # Append existing total expenses to the list
                    total_incomes_total_expenses.append(sum_of_ex_amount_values)
                elif sheet.title == "Expenses":
                    print("You need to specify: Type, Amount, Payment Method, and Description.")
                    print("Example: Type (Electric bill), Amount (450)," 
                          "Payment method (Card, Cash), Description (This payment is for the electricity expenses.)."
                          )  
                    print("")
                    # append current date to data list as the first element of the list
                    data_list.append(current_date)
                    expense_type = input("Enter expense type\n>>  ").capitalize() 
                    data_list.append(expense_type)
                    amount = int(input("Enter expense amount\n>>  ")) 
                    data_list.append(amount)
                    payment_method = input("Enter expense Payment method\n>>  ").capitalize()
                    data_list.append(payment_method)
                    description = input("write a description for this expense\n>>  ").capitalize()
                    data_list.append(description) 
                    print("Adding data to expenses sheet...")
                    sheet.append_row(data_list)
                    data_list.clear()
                    print("Your inputs has been successfully saved in the worksheet.")
                    print("")
                    print("You can add more expenses to this worksheet by typing 'add',"
                          " view the content by typing 'info', or type 'exit' to exit the program."
                          )
                    
                    # Access sum of incomes amount
                    incomes_sheet = SHEET.worksheet("Incomes")
                    inc_amount_column = incomes_sheet.col_values(3)
                    inc_amount_values = inc_amount_column[1:]
                    sum_of_inc_amount_values = sum(int(value) for value in inc_amount_values)
                    # Append existing total incomes to the list
                    total_incomes_total_expenses.append(sum_of_inc_amount_values)

                    # Accessing amount column of the sheet to return sum of all amounts
                    expenses_amount_column = sheet.col_values(3)
                    expenses_amount_values = expenses_amount_column[1:]
                    sum_of_expenses_amount_values = sum(int(value) for value in expenses_amount_values)
                    # Append total expenses to the list
                    total_incomes_total_expenses.append(sum_of_expenses_amount_values)         
            else:
                print("Exiting the program...\nProgram cloesed.")
                break
        else:
            print("Wrong Entry!!!\nPlease type 'info', 'add' or 'exit'.")
    return total_incomes_total_expenses
        

def main():
    """
    Run all program functions
    """
    print("****Welcome to Expenses Tracker! We're here to help you track your expenses and incomes.****\n****Let's begin your financial journey.****")

    modify_or_display_sheet(select_sheet())
    

main()
