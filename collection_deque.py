from collections import deque
de = deque([1,2,3])

de.append(4)
print ("The deque after appending at right is : ")
print (de)

de.appendleft(5)
print ("The deque after appending at left is : ")
print (de)

de.pop()
print ("The deque after deleting from right is : ")
print (de)

de.popleft()
print ("The deque after deleting from left is : ")
print (de)