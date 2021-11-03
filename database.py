#https://www.codiculum.com/tutorial/2020/06/crud-operations-with-python-and-mysql/
import mysql.connector as connector

config = {
    'user': 'root',
    'password': 'pw',
    'host': 'localhost',
    #connect to a database that is already created
    'database': 'mydb'
}

db = connector.connect(**config)
cursor = db.cursor()
