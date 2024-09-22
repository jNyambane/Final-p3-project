import sqlite3

# Database name
DATABASE_NAME = "library.db"

class Book:
    def __init__(self, book_id, book_name, author_name, year_of_publish):
        
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name
        self.year_of_publish = year_of_publish

    @classmethod
    def add_book(cls, book_id, book_name, author_name, year_of_publish):
        try:
            # Use 'with' statement to ensure the connection is closed properly
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                # Insert the new book into the 'books' table
                cursor.execute('''
                    INSERT INTO books (book_id, book_name, author_name, year_of_publish)
                    VALUES (?, ?, ?, ?)
                ''', (book_id, book_name, author_name, year_of_publish))
                
                print(f"Book '{book_name}' added successfully.")
                return True  # Indicate success

        except sqlite3.Error as e:
            # Handle any database errors that occur
            print(f"Error occurred while adding book: {e}")
            return False  # Indicate failure

    @classmethod
    def delete_book(cls, book_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                # Delete the book with the given ID from the 'books' table
                cursor.execute('DELETE FROM books WHERE book_id = ?', (book_id,))
                
                if cursor.rowcount == 0:
                    # No rows affected, meaning the book was not found
                    print(f"Book with ID {book_id} not found.")
                    return False
                else:
                    print(f"Book with ID {book_id} deleted successfully.")
                    return True

        except sqlite3.Error as e:
            # Handle any database errors that occur
            print(f"Error occurred while deleting book: {e}")
            return False

    @classmethod
    def get_all_books(cls):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                # Select all books from the 'books' table
                cursor.execute('SELECT * FROM books')
                books = cursor.fetchall()

                if books:
                    # Create and return a list of Book objects
                    book_objects = [cls(book_id=row[0], book_name=row[1], author_name=row[2], year_of_publish=row[3]) for row in books]
                    for book in book_objects:
                        print(f"ID: {book.book_id}, Name: {book.book_name}, Author: {book.author_name}, Year of Publish: {book.year_of_publish}")
                    return book_objects
                else:
                    print("No books found.")
                    return []

        except sqlite3.Error as e:
            # Handle any database errors that occur
            print(f"Error occurred while fetching books: {e}")
            return []

    @classmethod
    def find_book_by_id(cls, book_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                # Select the book with the given ID from the 'books' table
                cursor.execute('SELECT * FROM books WHERE book_id = ?', (book_id,))
                row = cursor.fetchone()

                if row:
                    # Create and return a Book object
                    book = cls(book_id=row[0], book_name=row[1], author_name=row[2], year_of_publish=row[3])
                    print(f"Book Found - ID: {book.book_id}, Name: {book.book_name}, Author: {book.author_name}, Year of Publish: {book.year_of_publish}")
                    return book
                else:
                    print(f"Book with ID {book_id} not found.")
                    return None

        except sqlite3.Error as e:
            # Handle any database errors that occur
            print(f"Error occurred while fetching book by ID: {e}")
            return None

    def __repr__(self):
        return f"Book(book_id={self.book_id}, book_name='{self.book_name}', author_name='{self.author_name}', year_of_publish={self.year_of_publish})"


