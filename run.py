import gspread
from google.oauth2.service_account import Credentials
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
                return incomes
            elif choice == "2":
                print("Selecting Expenses sheet...")
                expenses = SHEET.worksheet("Expenses")
                print("Expenses sheet selected.")
                return expenses
            else:
                print("Selecting Summary sheet...")
                summaries = SHEET.worksheet("Summary")
                print("Summary sheet selected.")
                return summaries
            break
        else:
            print("Wrong Entry!!!")

def main():
    """
    Run all program functions
    """
    print("****Welcome to Expenses Tracker! We're here to help you track your expenses and incomes.****\n****Let's begin your financial journey.****")

    select_sheet()

main()
