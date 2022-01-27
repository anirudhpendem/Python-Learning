from collections import namedtuple

Student = namedtuple('Student',['name','age','DOB'])

S = Student('Shiva','23','25041997')


li = ['Manjeet', '19', '411997' ]

di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }

print ("The Student age using index is : ",end ="")
print (S[1])

print ("The Student name using keyname is : ",end ="")
print (S.name)


print ("The namedtuple instance using iterable is : ")
print (Student._make(li))


print ("The OrderedDict instance using namedtuple is : ")
print (S._asdict())
