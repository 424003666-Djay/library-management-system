# Library Management System

## Project Overview
This project is a web-based Library Management System developed using Django. It provides pages for viewing and managing books, borrowers, and borrowing records.

## Technology Stack
- **Programming Language:** Python
- **Web Framework:** Django
- **Database:** SQLite
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

## Main Features
- Home page
- Book listing and book management
- Borrower listing
- Borrowing records
- Add Book function
- Book borrowing function (pending verification due to an identified error)

## Project Structure
- `manage.py` — Django project management command entry point
- `config/` — Project configuration and URL routing
- `library/` — Library application code, templates, models, views, and tests
- `db.sqlite3` — Local SQLite database

## Setup and Run
1. Install Python.
2. Open a terminal in the directory containing `manage.py`.
3. Activate the project's virtual environment, if available.
4. Install the project's required Python packages using the provided dependency file, if available.
5. Run database migrations if required:
   `python manage.py migrate`
6. Start the development server:
   `python manage.py runserver`
7. Open `http://127.0.0.1:8000/` in a browser.

**Note:** The exact dependency installation command must be confirmed from the project's dependency file. The application has been tested locally; deployment has not been verified.

## Testing Status
The home page, Books, Borrowers, Borrowing Records, and Add Book pages were tested locally. A book issuance error was also identified: `BorrowingRecord() got unexpected keyword arguments: 'status'`. This issue is documented in GitHub Issue #1 and remains open pending investigation and retesting.

## Version Control
The source code is maintained in GitHub:

https://github.com/424003666-Djay/library-management-system

GitHub Issues are used to document identified problems. Branches, pull requests, and peer reviews should be documented only when they have actually been performed.

## Issue Tracking

Known issues are documented using GitHub Issues. GitHub Issue #1 records the book issuance error encountered during local testing. The issue remains open until the cause is investigated, the problem is addressed, and the application is retested.
