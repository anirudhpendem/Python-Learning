import requests

load = {'username' : 'someone', 'password':"something"}

receive = requests.post("https://httpbin.org/post", data = load)

print(receive.json())

receive_dictionary = receive.json()

print(receive_dictionary['form']['username'],receive_dictionary['form']['password'])