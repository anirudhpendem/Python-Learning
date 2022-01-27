import requests

url = "https://www.w3schools.com/xml/books.xml"

res = requests.post(url)

print(res.status_code)
print(res.content)