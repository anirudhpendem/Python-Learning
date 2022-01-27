"""import mysql.connector
mydb = mysql.connector.connect(host="localhost",user = "root", password="anirudh@0000",database="mydata")
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY ,name VARCHAR(20), address VARCHAR(30))")
#mycursor.execute("SHOW TABLES")
sql = "INSERT INTO customers (name,address)VALUES(%s,%s)"
val =  ('Richard', 'Sky st 331')
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")



import mysql.connector
mydb = mysql.connector.connect(host="localhost",user = "root", password="anirudh@0000",database="mydata")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE emp(emp_id INT AUTO_INCREMENT PRIMARY KEY ,emp_name VARCHAR(20),  emp_profile VARCHAR(30), emp_age INT)")
mycursor.execute("SHOW TABLES")
for i in mycursor:
	print(i)
sql = "INSERT INTO emp (emp_name,emp_profile,emp_age)VALUES(%s,%s,%s)"
val =  ('anil','android-developer',29)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")"""

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="anirudh@0000",
  database="mydata"
)
mycursor = mydb.cursor()
"""mycursor.execute("CREATE TABLE student(rollno INT, sname VARCHAR(20), branch VARCHAR(20))")
Q="insert into student(rollno,sname,branch)values(%s,%s,%s)"
V=(203,"entersoft","cse")
mycursor.execute(Q,V)"""
sql = "alter table student add palce varchar(20) default 'hyd' "
sql1 = "update student set palce = 'nlg' where rollno = 202"
sql2 = "alter table student rename column palce to place"
sql3 = "alter table student drop column place"
mycursor.execute(sql3)
mydb.commit()  