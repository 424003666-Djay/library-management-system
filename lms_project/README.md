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

## Team Members

Rivera, Bhea R.
Omar, Alicia May T.
Delave Jr., Jonathan P.
Mariñas, Jhonj V.

**Contribution Note:** The project is maintained as a team project. Individual contributions should be documented based on the actual work completed by each member.

## Technology Versions

- Python: Verify using `python --version`.
- Django: Verify using `python -m django --version`.
- Database: SQLite.
- Operating environment: Local development on Windows.

Record the actual version numbers from the development environment before final submission.

## Prerequisites

- Python installed on the computer.
- The project source code.
- A terminal and a web browser.
- The project's virtual environment and required dependencies, if available.

## Database Setup

From the directory containing `manage.py`, run:

```bash
python manage.py migrate
```

This applies the project's database migrations. Use fictional sample data only when preparing demonstration records.

## Running Tests

From the directory containing `manage.py`, run:

```bash
python manage.py test library
```

Record the actual test results after running the command. Do not report tests as passed unless they complete successfully.

## Environment Configuration

No `.env.example` configuration has been verified for this project. If the application requires environment variables, provide an `.env.example` file containing dummy values only. Never commit real passwords, tokens, or secrets.

## Local Execution

Start the development server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser. This is a local development address, not a public deployment URL.

## Version and Known Limitations

- Project version: 0.1.0 (documentation label; verify whether an official version has been assigned).
- The book issuance function has a known error documented in GitHub Issue #1.
- The cause has not yet been resolved and the function has not been successfully retested.
- Public deployment has not been verified.

## Usage and License

No project license has been verified or specified in this README. Confirm the intended license before permitting reuse or redistribution.
