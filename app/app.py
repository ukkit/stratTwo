import os
import mysql.connector

# Load environment variables
MYSQL_HOST = os.getenv('MYSQL_HOST', 'mysql')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

# Connect to MySQL
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

cursor = conn.cursor()
cursor.execute("SELECT DATABASE();")
database_name = cursor.fetchone()[0]
print(f"Connected to MySQL Database: {database_name}")

cursor.close()
conn.close()
