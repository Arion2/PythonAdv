import datetime
import os

current_datetime = datetime.datetime.now()



print("year:", current_datetime.year)
print("month:", current_datetime.month)
print("day:", current_datetime.day)
print("hour:", current_datetime.hour)
print("minute:", current_datetime.minute)
print("second:", current_datetime.second)
print("microsecond:", current_datetime.microsecond)

current_date = datetime.datetime.now().date()

print(current_date)

print("Year", current_date.year)
print("month", current_date.month)
print("day", current_date.day)




settime = datetime.datetime.now().time()

specific_time = datetime.date(2000,1,1)

print(specific_time.year)
print(specific_time.month)
print(specific_time.day)


future_date = current_datetime + datetime.timedelta(days=100)
past_date = current_datetime - datetime.timedelta(days=100)

print("date 100 days in the future", future_date)

print(future_date.month)
print(future_date.day)
print("--------------")
print(past_date.month)
print(past_date.day)


print("-------------- files")


teksti ="hello this is the text i\n want to wtite"


with open("example.txt","w") as file:
    file.write(teksti)


file_path = "example.txt"
file = open(file_path,"r")

content = file.read()
print(content)
file.close()


with open("example.txt","r") as file:
    lines = file.readlines()
    print(lines)



with open("example.txt","r") as file:
    line = file.readline()
    print(line)

with open("example.txt","a") as file:
    file.write("\nnew data appended")



if os.path.exists("example.txt"):
    print("file exists!")
