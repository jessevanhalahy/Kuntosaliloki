import sqlite3
def setup_database():
    connection = sqlite3.connect('database.db')
    try:
        with open('schema.sql', 'r') as f:
            sql_script = f.read()
        connection.executescript(sql_script)
        print("Tables created successfully from schema.sql!")
        cursor = connection.cursor()
        categories = [('Upper Body',), ('Legs',), ('Cardio',)]
        cursor.executemany("INSERT OR IGNORE INTO categories (name) VALUES (?)", categories)
        connection.commit()
        print("Initial categories added!") 
    except FileNotFoundError:
        print("Error: schema.sql not found. Make sure the file exists in this folder.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()
        print("Database connection closed.")

if __name__ == "__main__":
    setup_database()