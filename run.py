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

# incomes = SHEET.worksheet('Incomes')

# data = incomes.get_all_values()

# pprint(data)

def main():
    """
    Run all program functions
    """
    print("****Welcome to Expenses Tracker! We're here to help you track your expenses and incomes.****\n****Let's begin your financial journey.****")

main()
