import mysql.connector

def db_connection_funt():
    return mysql.connector.connect (
        host ="localhost",
        user ="root",
        database ="D5_PDBC",
        password = "prasad@2345"
        )
    print("sucessfull connected to DB .......")