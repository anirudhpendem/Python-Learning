import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="anirudh@0000"
)

print(mydb)