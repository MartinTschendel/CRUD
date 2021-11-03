import sqlite3

#import mysql.connector as connector
#from mysql.connector import connect, errorcode
from database_sqlite import cursor, db

try:
    sql_create = '''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username varchar(255) NOT NULL,
        password varchar(255) NOT NULL,
        created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
    
    cursor.execute(sql_create)
    db.commit()
    print("table created")

except sqlite3.Error as e:
    print(f"could not create table: {e}")
    exit(1)


