import sqlite3
from database import create_tables
from book_controller import add_book, delete_book, get_all_books, find_book_by_id
from author_controller import add_author, delete_author, get_all_authors, find_author_by_id

# Main menu for the library management system
def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Manage Books")
        print("2. Manage Authors")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            manage_books()
        elif choice == '2':
            manage_authors()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Manage Books CLI
def manage_books():
    while True:
        print("\nManage Books")
        print("1. Add a Book")
        print("2. Delete a Book")
        print("3. View All Books")
        print("4. Find a Book by ID")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == '1':
            add_book_cli()
        elif choice == '2':
            delete_book_cli()
        elif choice == '3':
            view_all_books_cli()
        elif choice == '4':
            find_book_by_id_cli()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

# Manage Authors CLI
def manage_authors():
    while True:
        print("\nManage Authors")
        print("1. Add an Author")
        print("2. Delete an Author")
        print("3. View All Authors")
        print("4. Find an Author by ID")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == '1':
            add_author_cli()
        elif choice == '2':
            delete_author_cli()
        elif choice == '3':
            view_all_authors_cli()
        elif choice == '4':
            find_author_by_id_cli()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

# CLI function to add a book
def add_book_cli():
    print("\nAdd a New Book")
    book_id = input("Enter book ID: ")
    book_name = input("Enter book name: ")
    author_name = input("Enter author name: ")
    year_of_publish = input("Enter year of publish: ")

    if add_book(book_id, book_name, author_name, year_of_publish):
        print("Book added successfully!")
    else:
        print("Failed to add book.")

# CLI function to delete a book
def delete_book_cli():
    print("\nDelete a Book")
    book_id = input("Enter the book ID to delete: ")

    if delete_book(book_id):
        print(f"Book with ID {book_id} deleted successfully!")
    else:
        print(f"Book with ID {book_id} could not be found.")

# CLI function to view all books
def view_all_books_cli():
    print("\nView All Books")
    books = get_all_books()

    if not books:
        print("No books found in the library.")
    else:
        print("Books in the library:")
        for book in books:
            print(f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Year: {book[3]}")

# CLI function to find a book by ID
def find_book_by_id_cli():
    print("\nFind a Book by ID")
    book_id = input("Enter book ID: ")

    book = find_book_by_id(book_id)

    if book:
        print(f"Book Found - ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Year: {book[3]}")
    else:
        print(f"Book with ID {book_id} not found.")

# CLI function to add an author
def add_author_cli():
    print("\nAdd a New Author")
    author_id = input("Enter author ID: ")
    author_name = input("Enter author name: ")

    if add_author(author_id, author_name):
        print("Author added successfully!")
    else:
        print("Failed to add author.")

# CLI function to delete an author
def delete_author_cli():
    print("\nDelete an Author")
    author_id = input("Enter the author ID to delete: ")

    if delete_author(author_id):
        print(f"Author with ID {author_id} deleted successfully!")
    else:
        print(f"Author with ID {author_id} could not be found.")

# CLI function to view all authors
def view_all_authors_cli():
    print("\nView All Authors")
    authors = get_all_authors()

    if not authors:
        print("No authors found in the library.")
    else:
        print("Authors in the library:")
        for author in authors:
            print(f"ID: {author[0]}, Name: {author[1]}")

# CLI function to find an author by ID
def find_author_by_id_cli():
    print("\nFind an Author by ID")
    author_id = input("Enter author ID: ")

    author = find_author_by_id(author_id)

    if author:
        print(f"Author Found - ID: {author[0]}, Name: {author[1]}")
    else:
        print(f"Author with ID {author_id} not found.")

# Initialize the database and create tables
if __name__ == "__main__":
    create_tables()  # Ensure that tables are created
    main_menu()      # Start the CLI
