dict = {"colour" : ["RED","Green","Black","Blue"], "Place" : "Hyderabad", "State" : "Telangana", "Name" : "Entersoft", "Profile" : "Python-Dev"}
print(dict)
print(dict["Place"])
print(len(dict))
print(dict["colour"])
print(type(dict))
print(type(dict["colour"]))
a = dict
print(a)
b = dict["colour"]
print(b)
c = dict.get("Name")
print(c)
d = dict.keys()
print(d)
e = dict.values()
print(e)
print(dict.items())
print(dict.pop("State"))
print(dict)
