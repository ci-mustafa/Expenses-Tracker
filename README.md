# Expenses Tracker

Expenses Tracker is a Python terminal program that allows users to save and view their incomes and expenses. It also provides a summary of the remaining balance by calculating the difference between incomes and expenses. 

This program runs in the Code Institute mock terminal on Heroku.

[Here is the live verion of this project]( https://wallet-watcher-ee66c311b54b.herokuapp.com/)

![](/images/project_image.png)

## Table of Contents
### [How does this program work](#how-does-this-program-work-1)
### [Logic Flowchart](#logic-flowchart-1)
### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
### [Features](#features-1)
* [Existing Features](#existing-features)
### [Features Left to Implement](#features-left-to-implement-1)
### [Design](#design-1)
### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
### [Bugs](#bugs-1)
### [Deployment](#deployment-1)
### [Credits](#credits-1)
### [Content](#content-1)
### [Acknowledgements](#acknowledgements-1)
---

## How does this program work
The Expenses Tracker program operates by offering users a structured interface to manage their financial data across different sheets: Incomes, Expenses, and Summary. Upon launching the program, users are prompted to select a sheet from these options, with inputs validated to ensure correctness. Once a sheet is chosen, users are presented with several options: viewing the existing data on the sheet, adding new data, or exiting back to the main menu.

If a selected sheet is empty, users receive a message prompting them to either add data to populate the sheet or exit to the main menu. Notably, if a user selects the Expenses sheet and attempts to add expenses while the Incomes sheet remains empty, they are restricted from adding expenses until income data is entered.

Additionally, users can interact with the Summary sheet solely by viewing its content or choosing to exit, as attempts to manually add data are met with a clear message indicating that manual entries are not permitted in the Summary sheet.

After performing their desired operations on any sheet, users are given the option to exit the program.

## Logic flowchart
![Flowchart](/images/flow-chart-1.png)

## User Experience (UX)

The Expenses Tracker program is a comprehensive tool designed to help users manage their financial data efficiently. It provides a structured interface that segregates data into three main sheets: Incomes, Expenses, and Summary. The program ensures data integrity by validating inputs and guiding users through the process of tracking their finances.

### User Stories

* First-Time Visitors
    * Familiarization: Understand the layout and functionality of the program.
    * Initial Setup: Enter initial income data to begin tracking expenses.
    * Navigation: Learn how to navigate between different sheets and perform basic operations.

* Returning Visitors
    * Data Entry: Add new income and expense data as it occurs.
    * Data Review: View and review existing data to monitor financial status.
    * Summary Insights: Check the Summary sheet for an overview of their financial situation.

* Frequent Visitors
    * Regular Updates: Maintain up-to-date financial records by regularly entering data.
    * Detailed Monitoring: Closely monitor expenses and incomes to manage finances effectively.
    * Consistent Review: Frequently review the Summary sheet to ensure financial goals are being met.

---

## Features

### Existing Features

-   Google Sheets Integration: 
    - Data is stored in three separate Google Sheets for Incomes, Expenses, and Summary, ensuring easy  access and cloud-based storage.
    - Separate sheets for Incomes, Expenses, and Summary to organize data efficiently.
    - Ensures correctness of inputs and guides users to maintain accurate records.
    - Prevents adding expenses without entering incomes first.
    - Only viewable, ensuring that users cannot manually alter summary data.

    ![](/images/sheets.png)
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

---

## Design

* Flowchart
    * [Draw.io](http://draw.io/)

---

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

## Frameworks, Libraries & Programs Used

* [Gitpod](https://www.gitpod.io/)
    * To write the code.
* [Git](https://git-scm.com/)
    * for version control.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Draw.io](http://draw.io/)
    * To create a logic flowchart of the hangman game.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.
* [I Am Responsive](https://ui.dev/amiresponsive)
    * To ensure the program displays optimally on various devices
* [Pandas Library](https://pypi.org/project/pandas/)
    * To display data in a structured and tabular format, the program utilizes the Pandas library to present data in a DataFrame style.

## Testing
-   I have manually tested this project using the following steps:
    - CI Python Linter was used to test run.py

        <details>
        <summary> run.py CI Python Linter check
        </summary>

        ![](/images/ci-python-linter.png)
        </details>

    -   PEP8 Compliance:
        -   Passed the code through a PEP8 linter and corrected any issues to ensure compliance with Python's style guide.
        -   Confirmed that there are no remaining problems related to code style and formatting.

            <details>
            <summary> run.py PEP8 check
            </summary>

            ![](/images/py-check.png)
            </details>
    -   Invalid Input Handling:
        -   Provided various invalid inputs to test the robustness of the input validation, ensuring that the application correctly handles unexpected data types and formats.

            <details>
            <summary> Selecting sheets validations
            </summary>

            ![](/images/intro-validation.png)
            </details>

            <details>
            <summary> Expenses sheet data entry validation
            </summary>
                

            ![](/images/expense-sheet-validtion.png)
            </details>

            <details>
            <summary> Summary sheet data entry validation
            </summary>

            ![](/images/summary-data-entry.png)
            </details>


            <details>
            <summary> Data entry validations
            </summary>
            String datatype columns validation:
            Minmum length 4



            ![](/images/mini-length.png)

            Maximum length 50

            ![](/images/max-leng.png)

            only space is not allowed

            ![](/images/only-space.png)

            only digits are not allowed

            ![](/images/only-digit.png)

            Number datatype columns validation:
            Zero or negative data entry

            ![](/images/zero-neg.png)

            maximum amount limit 

            ![](/images/max-amount.png)

            Datatype check

            ![](/images/datatype-check.png)

            </details>
    -   Manual Testing:
        -   Conducted tests in my local terminal to verify the functionality and performance of the code.
        -   Additionally, tested the project in the Code Institute's Heroku terminal.

            | Feature | Expected Result | Steps Taken | Actual Result |
            | ------- | -------------- | ----------- | ------------- |
            | Introduction Screen   | To display welcome message and instructions | None | As Expected |
            | Option to select a sheet   | To display a sheet content, add data to the sheet or exit the program | '1' for Incomes sheet, '2' for Expenses sheet, '3' for Summary sheet, '0' to exit the program | As Expected |
            | Sheet data entry validation | To prevent adding data to expenses sheet if incomes sheet is empty | Selecting the sheet, type 'add' to add data to the sheet | As Expected |
            | Dynamic data entry | To prevent adding data manually to summary sheet | Selecting the summary sheet, type 'add' to add data to the sheet | As Expected |
            | Sheet data display validation | To prevent viewing sheet content if sheet is empty | Selecting the sheet, type 'info' to display the sheet content | As Expected |
            | Return to main menu | To exit the current sheet and return to main menu | Selecting the sheet, type 'exit' to exit the current sheet | As Expected |
            | Dynamic entry for date columns | To add current system date in date columns of the sheets | Selecting the sheet, type 'add' to add data to the sheet | As Expected |
            | Simple data entry, step by step | To add data to the sheets | Selecting the sheet, type 'add' to add data to the sheet, enter data for source, amount, payment method and description | As Expected |
            | Display sheet content | To view sheet content | Selecting the sheet, type 'info' to view sheet content | As Expected |


---

## Bugs

### Solved Bugs
-   Issue: An error occurred when entering a decimal data type for the amount.
-   Solution: The data type of the 'amount' column was converted to 'float' to accept both floating point numbers and integers, ensuring seamless data entry and processing.

-   Issue: The program did not initially set a maximum amount for the Amount column, which could lead to excessively large entries and potential data integrity issues.
-   Solution: Implement a maximum amount limit for the Amount column to ensure users cannot enter values beyond a predefined threshold.

## Remaining Bugs
-   No bugs remaining

---

## Deployment
This project was deployed using Code Institute's Mock terminal for Heroku

### Deploying to Heroku

To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. Deployed site [Expenses Tracker]( https://wallet-watcher-ee66c311b54b.herokuapp.com/)

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [GitHub Repository Expenses Tracker](https://github.com/ci-mustafa/Expenses-Tracker)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.

### Local Clone

1. Log in to GitHub and locate [GitHub Repository Expenses Tracker](https://github.com/ci-mustafa/Expenses-Tracker)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

## Credits
-   I gained understanding of python through code institute lessons.
-   Code Institute: For providing the deployment terminal.
-   Google Sheets: For offering the service used to store data.

## Content

* Expenses Tracker.
* All content was written by the developer.

## Acknowledgements

 * My mentor Mitko Bachvarov provided helpful feedback.
 * Slack community for encouragement.




