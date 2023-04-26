import mysql.connector

def load_to_mysql(df, host, user, password, database,port, table):
    """
    Loads a Pandas DataFrame into a MySQL database table.
    Args:
        df (pandas.DataFrame): DataFrame to load into the database.
        host (str): MySQL database host.
        user (str): MySQL database user.
        password (str): MySQL database password.
        database (str): MySQL database name.
        table (str): MySQL table name to load the data into.
    """
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="api_de_project",
        port=3307
    )
    cursor = conn.cursor()



    # Insert the data into the table
    for index, row in df.iterrows():
        sql = f"INSERT INTO {table} (place_id, name, address, rating) " \
              f"VALUES (%s, %s, %s, %s)"
        val = (row["place_id"], row["name"], row["address"], row["rating"])
        cursor.execute(sql, val)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

