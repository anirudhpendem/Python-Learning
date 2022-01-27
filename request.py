import requests

#url = "https://www.w3schools.com/python/ref_requests_response.asp"


#r = requests.get(url) 
r = requests.delete("https://httpbin.org/delete")
print(r.content)

#print(r.url)

#print(r.text)

#print(r.headers['Content-Encoding'])
