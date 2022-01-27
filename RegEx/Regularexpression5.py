import re
def sub():
	
	text1 = "I am writing java program."
	
	print(re.sub(r"java", "python", text1))
	
	text2 = "The climate is very cool."

	print(re.sub(r" very cool", " so hot", text2))

sub()


text = "Python is High level Programming Language. "

print(re.sub(r"[a-z]","0",text))
