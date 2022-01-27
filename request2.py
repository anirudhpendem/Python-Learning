import requests

loads = {'t':34, 's':76, 'e':43, 'y' :'name','f':"pwd"}

receive = requests.get("https://httpbin.org/get",params = loads)

print(receive.text)