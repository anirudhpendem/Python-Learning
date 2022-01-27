import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user= "root",password="anirudh@0000",database="mydata")
mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
	print(x)




"""import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user= "root",password="anirudh@0000",database="mydata")
mycursor = mydb.cursor()

sql = "SELECT * FROM emp ORDER BY emp_name"
#sql = "SELECT * FROM emp ORDER BY emp_name DESC"
mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
	print(x)"""