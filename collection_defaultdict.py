from collections import defaultdict

Dict = {'user' : 'Anirudh','place': 'hyderabad', 'state': 'Telangana'}
print("Dictionary:")
print(Dict)
print(Dict['user'])
#print(Dict['password'])

print("*********************************************")

def main():
	return "Invalid data"
d = defaultdict(main)
d['a'] = 1
d['b'] = 2
d['c'] = 3

print("Defaultdict:")
print(d)
print(d['a'])
print(d['b'])
print(d['d'])