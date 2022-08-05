import mysql.connector as connection
import mysql.connector
from mysql.connector import Error
import logging
logging.basicConfig(filename='loginfo.log', level=logging.INFO,format='%(asctime)s %(levelname)s %(name)s  %(message)s')
class database:
    @staticmethod
    def create_database_connection():
        connection = None
        try:
            connection = mysql.connector.connect(host="localhost", database = 'ineourn',user="root", passwd="user@123",use_pure=True)
            print("MySQL Database connection successful")
        except Error as err:
            logging.exception(err)
            print(f"Error: '{err}'")

        return connection
    @staticmethod
    def execute_query(conn, query):
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            print("Query executed successfully...")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def read_query(connection, query):
       cursor = connection.cursor()
       result = None
       try:
           cursor.execute(query)
           result = cursor.fetchall()
           return result
       except Error as err:
           print(f"Error: '{err}'")
