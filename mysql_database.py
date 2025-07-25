pip install mysql-connector-python
import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database_name"
    )
    print("Connection established successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
if 'conn' in locals() and conn.is_connected():
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John Doe", "123 Main St")
    cursor.execute(sql, val)
    conn.commit() 

    cursor.execute("SELECT * FROM customers")
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    conn.close()
    print("Connection closed.")
