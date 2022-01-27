import mysql.connector
mydb = mysql.connector.connect(host="localhost",user = "root", password="anirudh@0000",database="mydata")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
#mycursor.execute("SELECT name, address FROM customers")
#sql = "SELECT * FROM customers where name = 'anirudh' "
#mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
	print(x)




"""import mysql.connector
mydb = mysql.connector.connect(host="localhost",user = "root", password="anirudh@0000",database="mydata")
mycursor = mydb.cursor()
sql = "SELECT * FROM emp"
sql = "SELECT emp_name,emp_profile  FROM emp"
#sql = "SELECT * FROM emp where emp_name = 'anirudh' "
mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
	print(x)"""