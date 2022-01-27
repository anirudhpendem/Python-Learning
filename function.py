"""
def function(string):
	print('welcome'+" " + string)
function('world')
function('programming')
function('Entersoft')
"""

def function(*string):
	print("The world is " + string[1])
function('beautiful', 'pleasant', 'extraordinary')

