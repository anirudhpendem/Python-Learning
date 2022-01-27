import datetime
import pytz
cur_time = datetime.datetime.now()

print("The Current time with attributes are :")

print("Year :",end ="")
print(cur_time.year)

print("Month :",end ="")
print(cur_time.month)

print("Day :",end ="")
print(cur_time.day)

print("Hour :",end ="")
print(cur_time.hour)

print("Minutes :",end ="")
print(cur_time.minute)

print("second :",end ="")
print(cur_time.second)

time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
print("The current time in India is:", end="")
print(time)