import requests

url = "http://demo.testfire.net/api/login"

url2 = "http://demo.testfire.net/api/account"

url3 = "http://demo.testfire.net/api/transfer"

url4 = "http://demo.testfire.net/api/feedback/submit"

url5 = "http://demo.testfire.net/api/admin/addUser"

url6 = "http://demo.testfire.net/api/admin/changePassword"

load = {"username" : "jsmith", "password" : "demo1234"}

load1 = {"toAccount":800006,"fromAccount": 800003,"transferAmount": 200}

load2 = {"name": "J Smith","email": "jsmtih@altoromutual.com","subject": "Amazing web design","message": "I like the new look of your applicaiton"}

load3 = {"firstname": "Bilbo","lastname": "Baggins","username": "bilbob","password1": "S3l3ctS0methingStr0ng5AsP@ssword","password2": "S3l3ctS0methingStr0ng5AsP@ssword"}

load4 = {"username": "jdoe","password1": "Th1s!sz3nu3Passv0rd","password2": "Th1s!sz3nu3Passv0rd"}


header = {"Authorization":"YW5OdGFYUm86WkdWdGJ6RXlNelE9OjlpbyM\\/RFc="}


head = "/ANIRUDH/ENTERSOFT" 

st = ""

st +=  str(header) + head

login = requests.post(url,json = load,headers=header,params = st)
login_status_check = requests.get(url,json=load,headers = header )
Account_info = requests.get(url,url2,json=load,headers = header)
Transfer_amount = requests.post(url3,json=load1,headers=header)
Feedback = requests.post(url4,json=load2,headers=header)
Add_user = requests.post(url5,json=load3,headers=header)
Admin_changePassword = requests.post(url6,json=load4,headers=header)

print(st)
print(login.status_code)
print(login.content)

print( login_status_check.status_code)
print( login_status_check.content)

print(Account_info.status_code)
print(Account_info.content)

print(Transfer_amount.status_code)
print(Transfer_amount.content)

print(Feedback.status_code)
print(Feedback.content)

print(Add_user.status_code)
print(Add_user.content)

print(Admin_changePassword.status_code)
print(Admin_changePassword.content)
