import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user = "root", password="anirudh@0000",database="mydata")
mycursor = mydb.cursor()
sql = "ALTER TABLE emp ADD emp_dept_id VARCHAR(20)"
sql1 = ("UPDATE emp SET emp_dept_id = 'E0107' WHERE emp_id = 7"),
("UPDATE emp SET emp_dept_id = 'E0108' WHERE emp_id = 8"),
("UPDATE emp SET emp_dept_id = 'E0109' WHERE emp_id = 9"),
mycursor.execute(sql1)
mycursor.execute("SELECT * FROM emp")
result = mycursor.fetchall()
for x in result:
	print(x)
mydb.commit()

mydb.close()
