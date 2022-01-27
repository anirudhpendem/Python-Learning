import requests

load = {'usename' : 'ram','password' : 'pwd'}

receive = requests.post("https://httpbin.org/post",data = load )

print(receive.text)