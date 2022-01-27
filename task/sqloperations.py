import mysql.connector
try:
	mydb = mysql.connector.connect(host = "localhost",user = "root",password = "anirudh@0000",database = "mydata")
	mycursor = mydb.cursor()
	query1 = "CREATE TABLE emp(emp_id INT AUTO_INCREMENT PRIMARY KEY ,emp_name VARCHAR(20),  emp_profile VARCHAR(30), emp_age INT)"
	sql = "INSERT INTO emp (emp_name,emp_profile,emp_age) VALUES(%s,%s,%s)"
	val =[('sindhu','assist engg',32),
	 	  ('venky','manager',45)]
	query2 = "ALTER TABLE emp ADD(emp_dept_id VARCHAR(20))"
	query3 = "ALTER TABLE emp MODIFY emp_dept_id VARCHAR(15)"
	query4 = "ALTER TABLE emp RENAME COLUMN emp_dept_id TO emp_deptid"
	query5 = "ALTER TABLE emp DROP COLUMN emp_deptid"
	query6 = "UPDATE emp SET emp_profile = 'asst.manager' WHERE emp_id =10"
	query7 = "DELETE FROM emp WHERE emp_id =9 "
	query8 = "DROP TABLE student"
	query9 = "SELECT * FROM emp ORDER BY emp_name"
	query10 ="SELECT * FROM emp ORDER BY emp_name DESC"
	query11 ="SELECT * FROM emp"
	query12 ="SELECT * FROM emp LIMIT 7"
	query13 ="SELECT * FROM emp LIMIT 7 OFFSET 3 "
	mycursor.execute(query11)
	for x in mycursor:
		print(x)
	mydb.commit()
except:
	mydb.rollback()

mydb.close()