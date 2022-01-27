import requests

url ="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Google_Chrome_icon_%28September_2014%29.svg/1200px-Google_Chrome_icon_%28September_2014%29.svg.png"

receive = requests.get(url)

with open(r"C:\Users\aniru\OneDrive\Desktop\Python_Learning\download.jpg","wb") as f:

	f.write(receive.content)

print(receive.status_code)
