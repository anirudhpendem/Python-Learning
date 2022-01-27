import math

sub1 = int(input("Enter the sub1 marks: "))
sub2 = int(input("Enter the sub2 marks: "))
sub3 = int(input("Enter the sub3 marks: "))
sub4 = int(input("Enter the sub4 marks: "))
sub5 = int(input("Enter the sub5 marks: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

#print("Total Marks = %d"  %total)
print("Total marks = {0}".format(total))
#print("Marks Percentage = %d"  %percentage)
print("Marks Percentage = {0}".format(percentage))

if(percentage == 100  and percentage <= 90):
    
    print("A+ Grade")

elif(percentage < 90 and percentage >= 80 ):
    
    print("A Grade")

elif(percentage < 80 and percentage >= 70):
    
    print("B Grade")

elif(percentage < 70 and percentage >= 60):
    
    print("C Grade")

elif(percentage < 60 and percentage >= 50):
   
    print("D Grade")

elif(percentage < 50 and percentage >= 40):
   
    print("E Grade")

else:
    
    print("Fail")
