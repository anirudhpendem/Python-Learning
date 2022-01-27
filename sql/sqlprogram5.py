import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user= "root",password="anirudh@0000",database="mydata")
mycursor = mydb.cursor()
sql = " UPDATE customers SET name ='ENTERSOFT' WHERE name = 'Hannah'"
mycursor.execute(sql)
"""mydb.commit()
print(mycursor.rowcount,"record affected.")"""
sql1 = "SELECT * FROM customers"
mycursor.execute(sql1)
result = mycursor.fetchall()
for x in result:
	print(x)