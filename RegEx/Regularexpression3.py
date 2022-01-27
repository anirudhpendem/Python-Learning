import re

string = "Today my topic about Regular Expression using python language 98745"

regx = r"([a-nA-N])"
regx1 = r"[('\d')]"
regx2 = ('Ex....s')
regx3 = ('^Today')
regx4 = ('98745$')
regx5 = ('.*')
regx6 = ('.+')
regx7 = ('.?')
regx8 = r"[('\D{5} E')]"

seq =(r"\AToday")
seq1 =(r"Regular\b") #seq1 = (r"\babout")
seq2 =(r"\Bage") #seq2 =(r"Express\B")
seq3 =(r"\d")
seq4 =(r"\D")
seq5 =(r"\s")
seq6 =(r"\S")
seq7 =(r"\w")
seq8 =(r"\W")
seq9 =(r"98745\Z")

print(re.findall(regx,string))
print(re.findall(regx1,string))
print(re.findall(regx2,string))
print(re.findall(regx3,string))
print(re.findall(regx4,string))
print(re.findall(regx5,string))
print(re.findall(regx6,string))
print(re.findall(regx7,string))
print(re.findall(regx8,string))

print(re.findall(seq,string))
print(re.findall(seq1,string))
print(re.findall(seq2,string))
print(re.findall(seq3,string))
print(re.findall(seq4,string))
print(re.findall(seq5,string))
print(re.findall(seq6,string))
print(re.findall(seq7,string))
print(re.findall(seq8,string))
print(re.findall(seq9,string))