import sqlite3

# Define the database name (path)
DATABASE_NAME = "library.db"

# Function to initialize and create the database tables
def create_tables():
    try:
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Create the 'books' table if it doesn't already exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY,
                book_name TEXT NOT NULL,
                author_name TEXT NOT NULL,
                year_of_publish INTEGER NOT NULL
            )
        ''')
        
        # Commit the changes
        conn.commit()
        print("Tables created successfully (if not already existing).")

    except sqlite3.Error as e:
        print(f"Error occurred while creating tables: {e}")
    
    finally:
        # Close the database connection
        conn.close()
        
# Function to initialize and create the database tables
def create_tables():
    try:
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create the 'books' table if it doesn't already exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY,
                book_name TEXT NOT NULL,
                author_name TEXT NOT NULL,
                year_of_publish INTEGER NOT NULL
            )
        ''')

        # Create the 'authors' table if it doesn't already exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS authors (
                author_id INTEGER PRIMARY KEY,
                author_name TEXT NOT NULL
            )
        ''')

        # Commit the changes
        conn.commit()
        print("Tables created successfully (if not already existing).")

    except sqlite3.Error as e:
        print(f"Error occurred while creating tables: {e}")
    
    finally:
        # Close the database connection
        conn.close()

# Call the function to create tables when the script runs
if __name__ == "__main__":
    create_tables()


# Call the function to create tables when the script runs
if __name__ == "__main__":
    create_tables()
