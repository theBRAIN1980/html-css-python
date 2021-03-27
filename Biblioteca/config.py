
import mysql.connector

def connect():
    return  mysql.connector.connect( 
            host="192.168.111.95",
            user="thebrain",
            passwd="pinky",
            database="biblioteca"
            )