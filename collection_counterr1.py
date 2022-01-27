from collections import Counter
my_data = Counter([1,2,5,6,3,2,1,5,4,3,6,1,2,2,2,1,3])
print(my_data)
my_data.update([1,3,2,1,3,2])
print(my_data)

c1 = Counter(A = 10, B = 15 , C = 20)
c2 = Counter(A = 15, B = 20 , C = 10)
c1.subtract(c2)
print(c1)