import sqlite3
from database import DATABASE_NAME

# Function to add an author
def add_author(author_id, author_name):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO authors (author_id, author_name)
            VALUES (?, ?)
        ''', (author_id, author_name))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Error adding author: {e}")
        return False

# Function to delete an author by ID
def delete_author(author_id):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM authors WHERE author_id = ?
        ''', (author_id,))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0  # Check if an author was deleted
    except sqlite3.Error as e:
        print(f"Error deleting author: {e}")
        return False

# Function to retrieve all authors
def get_all_authors():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()
        conn.close()
        return authors
    except sqlite3.Error as e:
        print(f"Error retrieving authors: {e}")
        return []

# Function to find an author by ID
def find_author_by_id(author_id):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors WHERE author_id = ?', (author_id,))
        author = cursor.fetchone()
        conn.close()
        return author
    except sqlite3.Error as e:
        print(f"Error finding author by ID: {e}")
        return None
