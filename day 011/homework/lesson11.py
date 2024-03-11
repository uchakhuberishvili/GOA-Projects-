#for loop

#დავალება 1

for i in range(1,51,):
    print(i * 5)

#დავალება 2

for i in range(2,22,2):
    print(i)

#დავალება 3

for i in range(5,11):
    print(i*i)

#დავალება 4

user_input = int(input("please enter your number:"))
if (user_input % 2):
    print(user_input * 3 + 1)
else:
    print(user_input // 2)

#while loop

#დავალება 5 

i = 1
while i < 11:
    print(i)
    i += 1

#დავალება 6


name = 0
while name != (quit):
 name = input("enter name: ")
 if name == ("quit"):
  print("succesfull")
else:
 print("failed")

#დავალება 7

num = 10
while num < 22:
    print(num)
    num += 2

#დავალება 8

number = -1
while number < 0:
    number = int(input("enter a positive number:"))
    if number > 0:
        print("good job")

#დავალება 9 

num = 0
while num < 11:
    print(num * num)
    num += 1
    