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
    print("Select an action: view the sheet's data or add new data?\n"
          "Type 'info' to see the data or 'add' to enter new data.\n"
          "If you want to exit the program type 'exit'.\n"
          )
    # Data list to store in sheets
    data_list = []

    # Get the current system date
    current_date = datetime.now().strftime("%Y-%m-%d")
    # append current date to data list as the first element of the list
    data_list.append(current_date)
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
                print("Current data shown. Type 'exit' to leave the program.")
            elif user_choice == "add":
                if sheet.title == "Summary":
                    print("Heads up: This sheet does not support manual data addition.\n"
                          "This sheet is read-only. Type 'info' to see its contents."
                          )
                elif sheet.title == "Incomes":
                    print("You need to specify: Source, Amount, Payment Method, and Description.")
                    print("Example: Source (Job salary), Amount (4000)," 
                          "Payment method (card, cash), Description (Salary from online job)."
                          )  
                    print("")
                    source = input("Enter the income source\n>>  ").capitalize() 
                    data_list.append(source)
                    amount = int(input("Enter the income amount\n>>  ")) 
                    data_list.append(amount)
                    payment_method = input("Enter the income Payment method\n>>  ").capitalize()
                    data_list.append(payment_method)
                    description = input("write a description for this income\n>>  ").capitalize()
                    data_list.append(description) 
                    print("Adding data to Incomes sheet...")
                    sheet.append_row(data_list)
                    print("Your inputs has been successfully saved in the worksheet.")
                    
                       
            else:
                print("Exiting the program...\nProgram cloesed.")
                break
        else:
            print("Wrong Entry!!!\nPlease type 'info', 'add' or 'exit'.")
        

def main():
    """
    Run all program functions
    """
    print("****Welcome to Expenses Tracker! We're here to help you track your expenses and incomes.****\n****Let's begin your financial journey.****")

    modify_or_display_sheet(select_sheet())

main()
