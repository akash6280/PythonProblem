
from mysql.connector import connect, Error


def get_connection(USERNAME, PASSWORD, DATABASE):
    try:
        connection = connect(
            host="localhost",
            user=USERNAME,
            password=PASSWORD,
            database=DATABASE,
        )
        print("Connection successful!")
        return connection
    except Error as e:
        print(e)
        return None
