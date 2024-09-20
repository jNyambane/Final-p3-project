# Library Management System

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This is a Command-Line Interface (CLI) based Library Management System built in Python using SQLite for the database. It provides functionality to manage books and authors in the library, allowing users to perform various CRUD operations (Create, Read, Update, Delete).

## Features
### Managing Books
-   Add a new book with details (ID, name, author, and year of publication).
-   Delete an existing book by its ID.
-   View all books in the library.
-   Find a book by its ID.

### Managing Authors
-   Add a new author with details (ID, name).
-   Delete an existing author by its ID.
-   View all authors in the library.
-   Find an author by their ID.

### Stores the Data
The Data is stored using SQLite, which saves all books and authors in a local database (library.db).

## Setup Instructions and installation
#### Prerequisites
-   Python 3.8 and above
-   pipenv for managing dependencies

To run the Tasks locally, follow these steps:
1. **Clone the repository:**

    -- git clone `git@github.com:jNyambane/Final-phase3-project.git`
    -- cd Final-phase3-project
    -- code ..

2. **Make sure python and it's dependencies are installed:**
    ie: run ```pipenv install``` to install the dependencies on your terminal.
3. **Activate the virtual environment**
    Run ```pipenv shell```
4. **Initialize the database**
    Run ```python lib/database.py``` on the terminal to initialize the table.
5. **Run the applications**
    Run ```python lib/cli.py``` on the terminal to start the CLI.

## Usage

Once you run the application, you will be presented with a simple menu for managing books and authors. Navigate the menu by entering the appropriate option number.

**Main Menu**
Library Management System
1. Manage Books
2. Manage Authors
3. Exit

**Books Menu**
Manage Books
1. Add a Book
2. Delete a Book
3. View All Books
4. Find a Book by ID
5. Back to Main Menu

**Authors Menu**
Manage Authors
1. Add an Author
2. Delete an Author
3. View All Authors
4. Find an Author by ID
5. Back to Main Menu


***Examples on Usage.***
Example
1.  Add a Book:
    Input book details (ID, Name, Author, Year of Publish)
    Example input:
    _*_
    Enter book ID: 001
    Enter book name: Chozi la heri
    Enter author name: Assumpta .K. Matei
    Enter year of publish: 2013
    _*_
2.  View All Books:
    Displays a list of all books with their details.
    Example output:
    _*_
    ID: 001, Name: Chozi la Heri, Author: Assumpta .K. Matei, Year: 2013
    _-_
3.  Find an Author by ID:
    Input the author ID, and the application will show the author if found.
    Example:
    _*_
    Enter author ID: 002
    Author Found - ID: 002, Name: Ken Walibora
    _*_

## Technologies Used

Python
Python3
SQL
sqlite3

## Contributing

The project contributed to :

- [Titus Ouko](https://github.com/costamay)
- [Kelvin Muriithi](https://github.com/KelvinMuriithi)

and maintained by:

- [Joshua Nyambane](https://github.com/Nyamsjosh)

## License

This project is licensed under the MIT License - see the LICENSE file for details.