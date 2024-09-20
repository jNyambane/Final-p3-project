import sqlite3

DATABASE_NAME = "library.db"  # Change this to your actual database name

def add_book(book_id, book_name, author_name, year_of_publish):
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Execute the query to insert the new book
        cursor.execute('''
            INSERT INTO books (book_id, book_name, author_name, year_of_publish)
            VALUES (?, ?, ?, ?)
        ''', (book_id, book_name, author_name, year_of_publish))
        
        # Commit the changes
        conn.commit()
        
        print(f"Book '{book_name}' added successfully.")
        return True  # Indicate success

    except sqlite3.Error as e:
        print(f"Error occurred while adding book: {e}")
        return False  # Indicate failure
    
    finally:
        # Always close the connection, even if an error occurred
        conn.close()

def delete_book(book_id):
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Execute the delete query
        cursor.execute('DELETE FROM books WHERE book_id = ?', (book_id,))
        
        # Commit the changes
        conn.commit()

        if cursor.rowcount == 0:
            print(f"Book with ID {book_id} not found.")
            return False
        else:
            print(f"Book with ID {book_id} deleted successfully.")
            return True

    except sqlite3.Error as e:
        print(f"Error occurred while deleting book: {e}")
        return False
    
    finally:
        # Always close the connection, even if an error occurred
        conn.close()

def get_all_books():
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Execute the query to fetch all books
        cursor.execute('SELECT * FROM books')
        books = cursor.fetchall()

        if books:
            for book in books:
                print(f"ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Year of Publish: {book[3]}")
        else:
            print("No books found.")

        return books

    except sqlite3.Error as e:
        print(f"Error occurred while fetching books: {e}")
        return []
    
    finally:
        # Always close the connection, even if an error occurred
        conn.close()

def find_book_by_id(book_id):
    try:
        # Connect to the database
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Execute the query to fetch the book by ID
        cursor.execute('SELECT * FROM books WHERE book_id = ?', (book_id,))
        book = cursor.fetchone()

        if book:
            print(f"Book Found - ID: {book[0]}, Name: {book[1]}, Author: {book[2]}, Year of Publish: {book[3]}")
            return book
        else:
            print(f"Book with ID {book_id} not found.")
            return None

    except sqlite3.Error as e:
        print(f"Error occurred while fetching book by ID: {e}")
        return None
    
    finally:
        # Always close the connection, even if an error occurred
        conn.close()
