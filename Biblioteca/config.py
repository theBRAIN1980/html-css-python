
import mysql.connector

def connect():
    return  mysql.connector.connect( 
            host="79.115.46.195",
            port="56601",
            user="thebrain",
            passwd="L@g1kS3rv3rDr@g0$,2016",
            database="biblioteca"
            )