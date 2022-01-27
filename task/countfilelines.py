file = (open(r"C:\Users\aniru\OneDrive\Desktop\Python_Learning\task\sqloperations.py","r").read())
count =0
x = file.split("\n")
for i in x:
    if i:
        count += 1    
print("The Number of lines in this file is:",end= " ")
print(count)




#USING COMMAND LINE ARGUMENT
"""import sys
file = (open(sys.argv[1],"r").read())
count = 0
x = file.split("\n")
for i in x:
    if i:
        count += 1    
print("The Number of lines in this file is:",end= " ")
print(count)"""


