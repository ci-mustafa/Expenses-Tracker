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
