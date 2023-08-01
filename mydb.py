import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Lj21@lonan!'
)


#prepare a cursor object 
cursorObject = dataBase.cursor()


#Create a database 
cursorObject.execute("CREATE DATABASE nani")

print("All Done!")