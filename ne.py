import requests

res = requests.get('http://www.google.com', auth = ('user','pass') )
print(res.status_code)
#print(res.content)
if res.status_code == 200 :

	print("Login successful")

else:

	print("login unsuccessful")