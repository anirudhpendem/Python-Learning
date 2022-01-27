import requests

myurl = "https://httpbin.org/post"

files = {'file' : open('test.txt','rb')}

getdata = requests.post(myurl,files=files)

print(getdata.text)