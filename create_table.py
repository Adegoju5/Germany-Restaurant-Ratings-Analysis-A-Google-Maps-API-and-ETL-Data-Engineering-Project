import mysql.connector
from mysql.connector import errorcode

def create_table(cursor):
    try:
        cursor.execute(
            "CREATE TABLE restaurants ("
            "id VARCHAR(255) NOT NULL,"
            "name VARCHAR(255) NOT NULL,"
            "address VARCHAR(255) NOT NULL,"
            "rating FLOAT,"
            "PRIMARY KEY (id)"
            ")"
        )
        print("Table created successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print("Error creating table: {}".format(err))

# Connect to the database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="api_de_project",
    port="3307"
)

# Create a cursor
cursor = db.cursor()

# Create the table if it doesn't exist
create_table(cursor)

# Close the cursor and database connection
cursor.close()
db.close()