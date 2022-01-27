import re

s = 'My name is ANIRUDH PENDEM working at Entersoft company in Hyderabad'

match = re.search('Entersoft', s)

print('Start Index:', match.start())
print('End Index:', match.end())




print("\n")
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "My 9 date of Birth April 30")

if match != None:

	print ("Match at index %s, %s, %s" % (match.start(), match.end(), match.span()))

	print ("Full match: %s" % (match.group(0)))

	print ("Month: %s" % (match.group(1)))

	print ("Day: %s" % (match.group(2)))

else:
	print ("The regex pattern does not match.")
