from mysql_connect import get_connection
from dotenv import dotenv_values

config = dotenv_values(".env")
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']
DATABASE = config['DATABASE']


def execute_query(query):
    connection = get_connection(USERNAME, PASSWORD, DATABASE)
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()


def execute_and_print_query(query):
    connection = get_connection(USERNAME, PASSWORD, DATABASE)
    with connection.cursor(buffered=True) as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            print(row)
        connection.commit()
