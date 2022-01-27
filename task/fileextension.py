import os
fileDirectory = r"C:\Users\aniru\OneDrive\Desktop\Python_Learning"
fileExtension =".jpg"
file = os.listdir(fileDirectory)
for i in file:
    if i.endswith(fileExtension):
        print(i)




# USING COMMAND LINE ARGUMENT
"""import sys
import os
fileDirectory = sys.argv[1]
fileExtension = sys.argv[2]
file = os.listdir(fileDirectory)
for i in file:
    if i.endswith(fileExtension):
        print(i)"""



