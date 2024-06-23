# Expenses Tracker

Expenses Tracker is a Python terminal program that allows users to save and view their incomes and expenses. It also provides a summary of the remaining balance by calculating the difference between incomes and expenses. 

This program runs in the Code Institute mock terminal on Heroku.

[Here is the live verion of this project](https://wallet-watcher-3e97ff5bba22.herokuapp.com/)

![](/images/project_image.png)

## How does this program work
The Expenses Tracker program operates by offering users a structured interface to manage their financial data across different sheets: Incomes, Expenses, and Summary. Upon launching the program, users are prompted to select a sheet from these options, with inputs validated to ensure correctness. Once a sheet is chosen, users are presented with several options: viewing the existing data on the sheet, adding new data, or exiting back to the main menu.

If a selected sheet is empty, users receive a message prompting them to either add data to populate the sheet or exit to the main menu. Notably, if a user selects the Expenses sheet and attempts to add expenses while the Incomes sheet remains empty, they are restricted from adding expenses until income data is entered.

Additionally, users can interact with the Summary sheet solely by viewing its content or choosing to exit, as attempts to manually add data are met with a clear message indicating that manual entries are not permitted in the Summary sheet.

After performing their desired operations on any sheet, users are given the option to exit the program.

## Features

### Existing Features

- Program instruction:
    - A clear instruction for users to work with this program.

    ![](/images/instruction-image.png)

- Adding Data to Incomes and Expenses Sheets:
    - Users can add new income or expense entries to track their financial transactions.

    ![](/images/add-image.png)
    
- Viewing Sheet Data:
    - Users can view their existing incomes, expenses and summaries entries in a neatly formatted table.

    ![](/images/view-image.png)

- Input Validation:
    - The program validates user inputs to prevent errors and ensure accurate data entry.

    ![](/images/input-validation1.png)

    ![](/images/input-validation2.png)

- Displaying Data in Table Form:
    - Data in all sheets are presented in a visually appealing table format using the pandas library.

    ![](/images/table-image.png)

### Features Left to Implement
#### Overview
We’re thrilled to announce a new feature that will automatically save a percentage of your remaining balance based on set conditions. This will streamline your savings process, making sure you can save efficiently according to your financial situation without the hassle of manual adjustments. Plus, we’re updating the summary sheet with a new column to show the percentage saved, giving you a clearer picture of your financial progress.
-   Predefined Conditional Savings Rules:

    -   The system will include predefined rules that determine the savings percentage based on the remaining balance.
    -   Example Rule: "If the remaining balance is greater than $5000, save 20%."
    -   Additional rules can include:
        -   If the remaining balance is between $2000 and $5000, save 10%.
        -   If the remaining balance is less than $2000, save 5%.

## Testing
-   I have manually tested this project using the following steps:
    -   PEP8 Compliance:
        -   Passed the code through a PEP8 linter and corrected any issues to ensure compliance with Python's style guide.
        -   Confirmed that there are no remaining problems related to code style and formatting.
    -   Invalid Input Handling:
        -   Provided various invalid inputs to test the robustness of the input validation, ensuring that the application correctly handles unexpected data types and formats.
    -   Terminal Testing:
        -   Conducted tests in my local terminal to verify the functionality and performance of the code.
        -   Additionally, tested the project in the Code Institute's Heroku terminal.

