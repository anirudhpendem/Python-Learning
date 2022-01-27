
data = {"name" : "ANIRUDH", 
        
        "company" : " Entersoft",

        "location" : "Hyderabad",

        " State" : "Telangana",

        "Country" : "India"

         }

print(data)
print(data['Country'])
#print(data[2])
print(data.keys())
print(data.values())
#print(data[1:3])
data.update({"language" : "python"})
print(data)
data.pop('name')
print(data)
print(data.popitem())
print(len(data))
data.clear()
print(data)


