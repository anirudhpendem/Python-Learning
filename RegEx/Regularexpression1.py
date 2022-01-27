import re

print(r"\w print all equivalent to [a-zA-Z0-9_] ")
p = re.compile(r'\w')
print(p.findall("Python language * is easy to learn 987."))
print("\n")

print(r"\w+ matches to group of alphanumeric character")
p = re.compile(r'\w+')
print(p.findall("I went to start programming at 10 A.M., about \   *** in Reg_Ex 987."))
print("\n")

print(r"\W matches to non alphanumeric characters")
p = re.compile(r'\W')
print(p.findall("python  *** is some_language 987 # @ & ( !^+=;."))
print("\n")


