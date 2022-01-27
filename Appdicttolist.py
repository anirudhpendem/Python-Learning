#Syntax: list=[dict(zip([key],[x])) for x in range(start,stop)]

#where, key is the key and range() is the range of values to be appended

#Example: Python code to append 100 values from 1 to 100 with 1 as key to list
l = [dict(zip([1],[x])) for x in range(1,100)]
  
# display list
print(l)


