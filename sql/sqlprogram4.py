import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user= "root",password="anirudh@0000",database="mydata")
mycursor = mydb.cursor()

sql = "DELETE FROM customers where name = 'peter'"
mycursor.execute(sql)
sql1 = "SELECT * FROM customers"
mycursor.execute(sql1)
#print(mycursor.rowcount,"record deleted.")
#result = mycursor.fetchall()
for x in mycursor:
	print(x)





"""import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user= "root",password="anirudh@0000",database="mydata")
mycursor = mydb.cursor()

sql = "DELETE FROM emp where emp_name = 'anil'"
#print(mycursor.rowcount,"record deleted.")
sql = "SELECT * FROM emp"
mycursor.execute(sql)
#result = mycursor.fetchall()
for x in mycursor:
	print(x)"""