import json

blog = {'URL' : 'http://datacamp.com', 'name' : 'Datacamp'}

data = json.dumps(blog)

print(data)