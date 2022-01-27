n = int(input("Enter number of student :"))

res = {}

for i in range(n):

	print("Enter Deatils of student no.", i+i)

	Name = input("Name : ")

	Rollno = int(input("Rollno : "))

	Marks = int(input("Marks : "))

	res[Rollno] = [Name,Marks]

	print(res)

	for stu in res:

		if res[stu][1]>75:

			print(res[stu][0])