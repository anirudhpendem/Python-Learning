# Initialize the first five rows
n = 5

# Start the loop to print the first five rows
for i in range(5):
    for j in range(i):
        print('* ', end="")
    print('')

""" Start the loop to print the remaining rows in decreasing order of stars
for i in range(n,0,-1):
    for j in range(5):
        print('* ', end="")
    print('')"""