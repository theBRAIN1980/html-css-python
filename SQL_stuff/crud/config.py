#import the module
import mysql.connector
def connect():
    return  mysql.connector.connect( 
            host="127.0.0.1",
            user="root",
            passwd="",
            database="magazin"
            )