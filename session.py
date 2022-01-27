import requests

s = requests.get("http://www.google.com")

s.cookies

for cookie in s.cookies:
	print("cookie domain =" + cookie.domain)
	print("cookie name =" + cookie.name)
	print("cookie value =" + cookie.value)
	print("******************************")