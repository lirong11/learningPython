import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.2.37",
    user="root",
    passwd="123456"
)
print(mydb)
