import mysql.connector
import os
from datetime import datetime

# MySQL connection details
DB_CONFIG = {
    "host": "localhost",
    "user": "your_user",
    "password": "your_password",
    "database": "file_index_db",
}

# Directory to index
TARGET_DIRECTORY = "/path/to/your/files"

def create_table(cursor):
    """Creates the file_metadata table if it doesn't exist."""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS file_metadata (
                id INT AUTO_INCREMENT PRIMARY KEY,
                filepath VARCHAR(1000) NOT NULL,
                filename VARCHAR(255) NOT NULL,
                extension VARCHAR(50),
                size BIGINT,
                modification_date DATETIME
            )
        """)
        print("Table 'file_metadata' created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

def index_files(directory_path):
    """Scans the directory and indexes files in the database."""
    try:
        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor()
        create_table(cursor)

        for root, _, files in os.walk(directory_path):
            for file in files:
                full_path = os.path.join(root, file)
                filename, extension = os.path.splitext(file)
                size = os.path.getsize(full_path)
                mod_time = datetime.fromtimestamp(os.path.getmtime(full_path))

                insert_query = """
                    INSERT INTO file_metadata 
                    (filepath, filename, extension, size, modification_date) 
                    VALUES (%s, %s, %s, %s, %s)
                """
                data = (full_path, filename, extension, size, mod_time)
                cursor.execute(insert_query, data)
                cnx.commit()
                print(f"Indexed: {full_path}")

    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    index_files(TARGET_DIRECTORY)