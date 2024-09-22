import sqlite3
from database import DATABASE_NAME

class Author:
    def __init__(self, author_id, author_name):
        self.author_id = author_id
        self.author_name = author_name

    @classmethod
    def add_author(cls, author_id, author_name):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO authors (author_id, author_name)
                    VALUES (?, ?)
                ''', (author_id, author_name))
                return True
        except sqlite3.Error as e:
            print(f"Error adding author: {e}")
            return False

    @classmethod
    def delete_author(cls, author_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    DELETE FROM authors WHERE author_id = ?
                ''', (author_id,))
                return cursor.rowcount > 0  # Check if an author was deleted
        except sqlite3.Error as e:
            print(f"Error deleting author: {e}")
            return False

    @classmethod
    def get_all_authors(cls):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM authors')
                authors = cursor.fetchall()
                return [cls(author_id=row[0], author_name=row[1]) for row in authors]
        except sqlite3.Error as e:
            print(f"Error retrieving authors: {e}")
            return []

    @classmethod
    def find_author_by_id(cls, author_id):
        try:
            with sqlite3.connect(DATABASE_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM authors WHERE author_id = ?', (author_id,))
                row = cursor.fetchone()
                if row:
                    return cls(author_id=row[0], author_name=row[1])
                return None
        except sqlite3.Error as e:
            print(f"Error finding author by ID: {e}")
            return None

    def __repr__(self):
        return f"Author(author_id={self.author_id}, author_name='{self.author_name}')"
