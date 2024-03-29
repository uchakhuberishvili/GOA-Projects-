#1

list = ["ucha","giorgi","luka","data","nica","nana","mamuka"]
print(list[1],list[5],list[0],list[2],list[4],list[3],list[6])

#2

list = [1,2,3,4,5,6,7,8,9,10]
print(list[0],list[9])

#3

list = [10,11,12,13,14,15,16,17,18,19,20]
list[0] = 1
list[2] = 1
list[4] = 1
list[6] = 1
list[8] = 1
list[10] = 1
#4

name = input("please enter your name: ")
lastname = input("please enter your last name: ")
age = input("please enter your age: ")
location = input("please enter your location: ")
email = input("please enter your email: ")
list = [name,lastname,age,location,email]
print(list)

#5

name1 = "ucha"
for i in range(0,len(name1)):
    print(name1[1])
