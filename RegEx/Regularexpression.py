import re

string = "My phone number is 9876543210 and My office number is 04012345678"

result = re.findall("\d+",string)

print(result)