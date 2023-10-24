
import mysql.connector


dataBase = mysql.connector.connect(
    host= 'localhost',
    user= 'arhantbararia',
    passwd = 'arh123',

)



cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE client_data")

print("DATABASE created!")