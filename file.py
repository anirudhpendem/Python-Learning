fileobj = open("myfile.txt","w")
fileobj.write("python is a programming language")
fileobj = open("myfile.txt","r+")
print(fileobj.read())
fileobj.close()