A = ["\n Entersoft", "\n Cyber-security", "\n Application", "\n Cloud-computing", "\n Python-Developer"]
fileobj = open("myfile1.txt","w")
fileobj.write("\n python is simple to understand  programming language")
fileobj.write("\n New File Created as myfile1")
fileobj.writelines(A)
fileobj.close()
fileobj = open("myfile1.txt","r+")
print(fileobj.read())
fileobj.seek(0)

print("output of readline")
print(fileobj.readline())
print()
fileobj.seek(0)
  
# To show difference between read and readline 
print("Output of Read(9) function is ")
print(fileobj.read(9))
print()
  
fileobj.seek(0)
  
print("Output of Readline(9) function is ")
print(fileobj.readline(9))
print()
  
fileobj.seek(0)
  
# readlines function 
print("Output of Readlines function is ")
print(fileobj.readlines())
print()
fileobj.close() 